Write-Host "Autorisation d'execution pour cette session" -ForegroundColor Yellow
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
Write-Host "Generation du venv" -ForegroundColor Green
try {
    python -m venv venv
    if ($LASTEXITCODE -ne 0) {
        throw "La creation du venv a echoue."
    }

    Write-Host "Venv cree, activation..." -ForegroundColor Green
    .\venv\Scripts\Activate.ps1

    if ($LASTEXITCODE -ne 0) {
        throw "L'activation du venv a echoue." 
    }

    Write-Host("Installation des dependances python")
    python -m pip install -r requirement.txt
    if ($LASTEXITCODE -ne 0){
        throw "L'installation des dépendances a echoue" 
    }

    Write-Host "Lancement du programme de gestion de paiement" -ForegroundColor Green
    python .\main.py
}
catch {
    Write-Host "Erreur : $_" -ForegroundColor Red
}