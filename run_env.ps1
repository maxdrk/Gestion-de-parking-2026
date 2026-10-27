Write-Host "Autorisation d'exécution pour cette session" -ForegroundColor Yellow
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
Write-Host "Génération du venv" -ForegroundColor Green
try {
    python -m venv venv
    if ($LASTEXITCODE -ne 0) {
        throw "La création du venv a échoué."
    }

    Write-Host "Venv créé, activation..." -ForegroundColor Green
    .\venv\Scripts\Activate.ps1

    Write-Host "Lancement du programme d'entrée et de sortie du parking" -ForegroundColor Green
    python .\main.py
}
catch {
    Write-Host "Erreur : $_" -ForegroundColor Red
}