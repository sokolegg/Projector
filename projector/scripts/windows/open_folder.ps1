<#
.SYNOPSIS
./open_folder.ps1
.DESCRIPTION
Opens the folder you specified in Windows Explorer.
.EXAMPLE
./open_folder.ps1 -FolderPath C:\Temp
#>
param(
    [CmdletBinding()]
    [Parameter(Mandatory)]
    [string]$FolderPath
)
try {
start-process explorer.exe -ArgumentList $FolderPath;
}
catch {
throw "Folder path is not specified"
}
