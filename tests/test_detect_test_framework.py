import importlib.util
import json
from pathlib import Path


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "skills"
    / "test-generator"
    / "scripts"
    / "detect_test_framework.py"
)


def load_detector_module():
    spec = importlib.util.spec_from_file_location(
        "detect_test_framework",
        SCRIPT_PATH,
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


detector = load_detector_module()


def test_detects_pytest_from_pyproject(tmp_path):
    pyproject = tmp_path / "pyproject.toml"
    pyproject.write_text(
        """
[project]
name = "sample-project"

[dependency-groups]
dev = ["pytest"]
""",
        encoding="utf-8",
    )

    result = detector.detect_test_framework(tmp_path)

    assert result["language"] == "python"
    assert result["framework"] == "pytest"
    assert result["confidence"] == "high"
    assert "pyproject.toml contains 'pytest'" in result["evidence"]


def test_detects_pytest_from_requirements(tmp_path):
    requirements = tmp_path / "requirements.txt"
    requirements.write_text(
        """
flask
pytest
requests
""",
        encoding="utf-8",
    )

    result = detector.detect_test_framework(tmp_path)

    assert result["language"] == "python"
    assert result["framework"] == "pytest"
    assert result["confidence"] == "high"


def test_detects_jest_from_package_json_dependencies(tmp_path):
    package_json = tmp_path / "package.json"
    package_json.write_text(
        json.dumps(
            {
                "name": "sample-js-project",
                "devDependencies": {
                    "jest": "^29.0.0",
                },
                "scripts": {
                    "test": "jest",
                },
            }
        ),
        encoding="utf-8",
    )

    result = detector.detect_test_framework(tmp_path)

    assert result["language"] == "javascript/typescript"
    assert result["framework"] == "jest"
    assert result["confidence"] == "high"


def test_detects_vitest_from_package_json_dependencies(tmp_path):
    package_json = tmp_path / "package.json"
    package_json.write_text(
        json.dumps(
            {
                "name": "sample-vite-project",
                "devDependencies": {
                    "vitest": "^1.0.0",
                    "vite": "^5.0.0",
                },
                "scripts": {
                    "test": "vitest",
                },
            }
        ),
        encoding="utf-8",
    )

    result = detector.detect_test_framework(tmp_path)

    assert result["language"] == "javascript/typescript"
    assert result["framework"] == "vitest"
    assert result["confidence"] == "high"


def test_prefers_vitest_when_vite_is_present(tmp_path):
    package_json = tmp_path / "package.json"
    package_json.write_text(
        json.dumps(
            {
                "name": "sample-vite-project",
                "devDependencies": {
                    "vite": "^5.0.0",
                    "jest": "^29.0.0",
                },
                "scripts": {
                    "test": "vitest",
                },
            }
        ),
        encoding="utf-8",
    )

    result = detector.detect_test_framework(tmp_path)

    assert result["language"] == "javascript/typescript"
    assert result["framework"] == "vitest"
    assert result["confidence"] == "high"


def test_detects_junit5_from_pom_xml(tmp_path):
    pom = tmp_path / "pom.xml"
    pom.write_text(
        """
<project>
    <dependencies>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>5.10.0</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
</project>
""",
        encoding="utf-8",
    )

    result = detector.detect_test_framework(tmp_path)

    assert result["language"] == "java"
    assert result["framework"] == "junit5"
    assert result["confidence"] == "high"


def test_detects_junit5_from_gradle(tmp_path):
    gradle = tmp_path / "build.gradle"
    gradle.write_text(
        """
dependencies {
    testImplementation 'org.junit.jupiter:junit-jupiter:5.10.0'
}
""",
        encoding="utf-8",
    )

    result = detector.detect_test_framework(tmp_path)

    assert result["language"] == "java"
    assert result["framework"] == "junit5"
    assert result["confidence"] == "high"


def test_returns_unknown_when_no_framework_is_detected(tmp_path):
    result = detector.detect_test_framework(tmp_path)

    assert result["language"] == "unknown"
    assert result["framework"] == "unknown"
    assert result["confidence"] == "none"
    assert result["evidence"] == []


def test_detects_python_test_files_with_low_confidence(tmp_path):
    tests_dir = tmp_path / "tests"
    tests_dir.mkdir()

    test_file = tests_dir / "test_calculator.py"
    test_file.write_text(
        """
def test_addition():
    assert 1 + 1 == 2
""",
        encoding="utf-8",
    )

    result = detector.detect_test_framework(tmp_path)

    assert result["language"] == "python"
    assert result["framework"] == "pytest"
    assert result["confidence"] == "low"
    assert "Python test files found" in result["evidence"]


def test_detects_javascript_test_files_with_low_confidence(tmp_path):
    test_file = tmp_path / "calculator.test.ts"
    test_file.write_text(
        """
test("adds numbers", () => {
  expect(1 + 1).toBe(2);
});
""",
        encoding="utf-8",
    )

    result = detector.detect_test_framework(tmp_path)

    assert result["language"] == "javascript/typescript"
    assert result["framework"] == "jest"
    assert result["confidence"] == "low"
    assert "JavaScript/TypeScript test files found" in result["evidence"]


def test_detects_java_test_files_with_low_confidence(tmp_path):
    test_file = tmp_path / "CalculatorTest.java"
    test_file.write_text(
        """
class CalculatorTest {
}
""",
        encoding="utf-8",
    )

    result = detector.detect_test_framework(tmp_path)

    assert result["language"] == "java"
    assert result["framework"] == "junit5"
    assert result["confidence"] == "low"
    assert "Java test files found" in result["evidence"]