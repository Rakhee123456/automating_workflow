<#
.SYNOPSIS
    Schedules auto_push.py to run daily at a specified time via Windows Task Scheduler.
.EXAMPLE
    .\setup_scheduler.ps1 -Time "09:00"
#>
param (
    [string]$Time = "09:00"
)

$TaskName = "GitHubDailyAutoCommit"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$PythonExe = (Get-Command python.exe -ErrorAction SilentlyContinue).Source

if (-not $PythonExe) {
    Write-Error "Python was not found in PATH. Please ensure Python is installed and accessible."
    exit 1
}

$ScriptPath = Join-Path $ScriptDir "auto_push.py"
$Action = New-ScheduledTaskAction -Execute $PythonExe -Argument "`"$ScriptPath`"" -WorkingDirectory $ScriptDir
$Trigger = New-ScheduledTaskTrigger -Daily -At $Time
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

Write-Host "Registering Windows Scheduled Task: $TaskName to run every day at $Time..." -ForegroundColor Cyan

try {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue
    Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Settings $Settings -Description "Automated 367-day GitHub commit and push task." | Out-Null
    Write-Host "[SUCCESS] Task '$TaskName' registered successfully!" -ForegroundColor Green
    Write-Host "It will run daily at $Time from directory: $ScriptDir" -ForegroundColor Green
} catch {
    Write-Error "Failed to register scheduled task: $_"
}
