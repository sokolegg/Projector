<#
.SYNOPSIS
./open_url.ps1
.DESCRIPTION
Starts Google Chrome browser with the link specified
.EXAMPLE
./open_url.ps1 -HostAddress 'https://google.com'
#>
param(
    [CmdletBinding()]
    [Parameter(Mandatory)]
    [string]$HostAddress
)
try {
start-process chrome.exe -ArgumentList $HostAddress;
}
catch {
throw "Host address is empty"
}
