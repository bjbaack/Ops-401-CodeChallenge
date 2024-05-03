Write-Host "Configuring password history to prevent password reuse..."
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters" -Name "PasswordHistorySize" -Value 24

Write-Host "Disabling SMB v1 server for security..."
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" -Name "SMB1" -Type DWORD -Value 0

$passwordHistorySize = Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters" -Name "PasswordHistorySize"
$smbv1Status = Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" -Name "SMB1"

Write-Host "Password History Size is set to: $($passwordHistorySize.PasswordHistorySize)"
Write-Host "SMB v1 Server is set to: $($smbv1Status.SMB1) (0 indicates disabled, 1 indicates enabled)"

Write-Host "It's recommended to restart your system to ensure all changes are properly applied."
