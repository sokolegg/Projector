<#
.SYNOPSIS
./open_folder.ps1
.DESCRIPTION
Opens the folder you specified with Windows Explorer.
.EXAMPLE
./open_folder.ps1 -FolderPath C:\Temp
#>
param(
    [CmdletBinding()]
    [Parameter(Mandatory=$true)]
    [string]$FolderPath
)
try {
if (test-path -path $FolderPath) {
start-process explorer.exe -ArgumentList $FolderPath;
}
else {
    write-host "Folder is not found" -Foregroundcolor Red -Backgroundcolor Black
}
}
catch [System.Management.ItemNotFoundException] {
$_.Exception.GetType().Name;
}
