param([Alias('TargetPath')][string]$p);$ErrorActionPreference=1;if(!$p.Trim()){$p=$PSScriptRoot};[void](gi -l $p -fo).CreateSubdirectory((Get-Date -f yyyy.MM.dd))
