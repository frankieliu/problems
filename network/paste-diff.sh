which=1
paste snmp${which}before.log snmp${which}after.log | awk '{print $1, $8-$4}' | grep -vP ' 0$' > snmp${which}diff.log

which=2
paste snmp${which}before.log snmp${which}after.log | awk '{print $1, $8-$4}' | grep -vP ' 0$' > snmp${which}diff.log
