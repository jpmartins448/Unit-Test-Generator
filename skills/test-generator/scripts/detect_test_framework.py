#!/usr/bin/env python3

"""
Detect the likely programming language and test framework used by a project.

This script is intentionally simple and dependency-free.
It scans common project files such as package.json, pyproject.toml,
requirements.txt, pom.xml, and build.gradle.

Example usage:

    python skills/test-generator/scripts/detect_test_framework.py .
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


SUPPORTED_FILES = [
    "package.json",
    "pyproject.toml",
    "requirements.txt",
    "requirements-dev.txt",
    "setup.cfg",
    "tox.ini",
    "pom.xml",
    "build.gradle",
    "build.gradle.kts",
]


def read_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def file_contains(path: Path, terms: list[str]) -> list[str]:
    content = read_file(path).lower()
    return [term for term in terms if term.lower() in content]


def detect_python_framework(root: Path) -> dict[str, Any] | None:
    evidence: list[str] = []

    python_files = [
        "pyproject.toml",
        "requirements.txt",
        "requirements-dev.txt",
        "setup.cfg",
        "tox.ini",
    ]

    for filename in python_files:
        path = root / filename
        if not path.exists():
            continue

        matches = file_contains(path, ["pytest", "unittest"])
        for match in matches:
            evidence.append(f"{filename} contains '{match}'")

    test_files = list(root.rglob("test_*.py")) + list(root.rglob("*_test.py"))

    if test_files:
        evidence.append("Python test files found")

    if any("pytest" in item.lower() for item in evidence):
        return {
            "language": "python",
            "framework": "pytest",
            "confidence": "high",
            "evidence": evidence,
        }

    if any("unittest" in item.lower() for item in evidence):
        return {
            "language": "python",
            "framework": "unittest",
            "confidence": "medium",
            "evidence": evidence,
        }

    if test_files:
        return {
            "language": "python",
            "framework": "pytest",
            "confidence": "low",
            "evidence": evidence,
        }

    return None


def detect_javascript_framework(root: Path) -> dict[str, Any] | None:
    evidence: list[str] = []

    js_test_files = (
        list(root.rglob("*.test.js"))
        + list(root.rglob("*.spec.js"))
        + list(root.rglob("*.test.ts"))
        + list(root.rglob("*.spec.ts"))
    )

    if js_test_files:
        evidence.append("JavaScript/TypeScript test files found")

    package_json = root / "package.json"

    if not package_json.exists():
        if js_test_files:
            return {
                "language": "javascript/typescript",
                "framework": "jest",
                "confidence": "low",
                "evidence": evidence,
            }

        return None

    try:
        data = json.loads(read_file(package_json))
    except json.JSONDecodeError:
        data = {}

    dependencies = {}
    dependencies.update(data.get("dependencies", {}))
    dependencies.update(data.get("devDependencies", {}))

    scripts = data.get("scripts", {})

    dependency_names = set(dependencies.keys())
    script_values = " ".join(str(value) for value in scripts.values()).lower()

    has_vitest = (
        "vitest" in dependency_names
        or "vitest" in script_values
        or "vite" in dependency_names
    )

    has_jest = (
        "jest" in dependency_names
        or "ts-jest" in dependency_names
        or "@types/jest" in dependency_names
        or "jest" in script_values
    )

    if has_vitest:
        evidence.append("package.json indicates Vitest or Vite")
        return {
            "language": "javascript/typescript",
            "framework": "vitest",
            "confidence": "high",
            "evidence": evidence,
        }

    if has_jest:
        evidence.append("package.json indicates Jest")
        return {
            "language": "javascript/typescript",
            "framework": "jest",
            "confidence": "high",
            "evidence": evidence,
        }

    return None


def detect_java_framework(root: Path) -> dict[str, Any] | None:
    evidence: list[str] = []

    java_build_files = [
        "pom.xml",
        "build.gradle",
        "build.gradle.kts",
    ]

    for filename in java_build_files:
        path = root / filename
        if not path.exists():
            continue

        matches = file_contains(path, ["junit-jupiter", "org.junit.jupiter", "junit"])
        for match in matches:
            evidence.append(f"{filename} contains '{match}'")

    java_test_files = list(root.rglob("*Test.java"))

    if java_test_files:
        evidence.append("Java test files found")

    if any("junit-jupiter" in item.lower() or "org.junit.jupiter" in item.lower() for item in evidence):
        return {
            "language": "java",
            "framework": "junit5",
            "confidence": "high",
            "evidence": evidence,
        }

    if any("junit" in item.lower() for item in evidence):
        return {
            "language": "java",
            "framework": "junit",
            "confidence": "medium",
            "evidence": evidence,
        }

    if java_test_files:
        return {
            "language": "java",
            "framework": "junit5",
            "confidence": "low",
            "evidence": evidence,
        }

    return None


def detect_test_framework(root: Path) -> dict[str, Any]:
    detectors = [
        detect_python_framework,
        detect_javascript_framework,
        detect_java_framework,
    ]

    results = []

    for detector in detectors:
        result = detector(root)
        if result is not None:
            results.append(result)

    if not results:
        return {
            "language": "unknown",
            "framework": "unknown",
            "confidence": "none",
            "evidence": [],
        }

    confidence_order = {
        "high": 3,
        "medium": 2,
        "low": 1,
        "none": 0,
    }

    results.sort(
        key=lambda item: confidence_order.get(item["confidence"], 0),
        reverse=True,
    )

    return results[0]


def main() -> None:
    root_arg = sys.argv[1] if len(sys.argv) > 1 else "."
    root = Path(root_arg).resolve()

    if not root.exists():
        print(
            json.dumps(
                {
                    "error": f"Path does not exist: {root}",
                },
                indent=2,
            )
        )
        sys.exit(1)

    result = detect_test_framework(root)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()