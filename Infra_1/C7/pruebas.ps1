find-module -name invokequery
install-module -name invokequery
Import-Module InvokeQuery
Get-Command -Module InvokeQuery
$creds = Get-Credential
$query = New-SqlQuery -sql "Select * from test"
$query 
Invoke-MySqlQuery -SqlQuery $query -Credential $creds -Server localhost -Database test

## clase 8 ;-;
