@echo off
REM Convenience launcher for Cognitive Genome – ApeTest v0.1
REM Assumes Python is on PATH and this .bat lives in the repo root or is called from there.

echo.
echo 🧬 Cognitive Genome – ApeTest v0.1
echo ---------------------------------
echo 1. Run ApeTest and collect raw responses
echo 2. Manually score a raw responses file
echo 3. (Advanced) LLM-based scoring stub
echo.

set /p choice="Select an option (1-3): "

if "%choice%"=="1" (
    python cli\ape_test_v0_1.py
    goto end
)

if "%choice%"=="2" (
    python cli\ape_score_v0_1.py
    goto end
)

if "%choice%"=="3" (
    python cli\ape_score_llm_v0_1.py
    goto end
)

echo Invalid choice.
:end
echo.
pause
