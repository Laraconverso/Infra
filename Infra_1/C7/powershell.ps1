find-module -Name invokequery
install-modue -name invokequery
$creds = Get-Credential
$query = New-SqlQuery -Sql "SELECT * FROM test"

Invoke-MySqlQuery -SqlQuery $query -Credential $creds