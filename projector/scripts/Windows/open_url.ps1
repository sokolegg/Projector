<#
.SYNOPSIS
./launchChrome.ps1
.DESCRIPTION
Starts Google Chrome browser with the link specified
.EXAMPLE
./launchChrome.ps1 -HostAddress 'https://google.com'
#>
param(
    [CmdletBinding()]
    [Parameter(Mandatory)]
    [string]$HostAddress
)
try {
start-process chrome.exe;
}
catch {
$HostAddress = $Null;
}
