Param(
  [string]$Email = ""
)
Write-Host "== Questify Collab Dev =="
if (!(Test-Path "backend/.venv")) {
  python -m venv backend/.venv
}
& backend/.venv/Scripts/python -m pip install -r backend/requirements.txt
Push-Location frontend; npm install; Pop-Location
if ($Email -ne "") {
  & backend/.venv/Scripts/python backend/scripts/seed_for_email.py --email "$Email"
}
Start-Process powershell -ArgumentList '-NoProfile','-Command','cd questify-collab; backend\.venv\Scripts\python -m uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 --reload'
Start-Process powershell -ArgumentList '-NoProfile','-Command','cd questify-collab\frontend; npm run dev'