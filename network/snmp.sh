if false; then
    snmpwalk -v2c -c abc 10.213.0.17 IF-MIB::ifHCInUcastPkts.38
    snmpwalk -v2c -c abc 10.213.0.17 IF-MIB::ifHCOutUcastPkts.38
    snmpwalk -v2c -c abc 10.213.0.17 IF-MIB::ifInDiscards.38
    snmpwalk -v2c -c abc 10.213.0.17 IF-MIB::ifOutDiscards.38
    snmpwalk -v2c -c abc 10.213.0.17 IF-MIB::ifHCInUcastPkts.2
    snmpwalk -v2c -c abc 10.213.0.17 IF-MIB::ifHCOutUcastPkts.2
    snmpwalk -v2c -c abc 10.213.0.17 IF-MIB::ifInDiscards.2
    snmpwalk -v2c -c abc 10.213.0.17 IF-MIB::ifOutDiscards.2
    snmpwalk -v2c -c abc 10.213.0.17 IF-MIB::ifHCInUcastPkts.1
    snmpwalk -v2c -c abc 10.213.0.17 IF-MIB::ifHCOutUcastPkts.1
    snmpwalk -v2c -c abc 10.213.0.17 IF-MIB::ifInDiscards.1
    snmpwalk -v2c -c abc 10.213.0.17 IF-MIB::ifOutDiscards.1
fi
snmpwalk -v2c -c abc 10.213.0.17 IF-MIB::ifHCInUcastPkts
snmpwalk -v2c -c abc 10.213.0.17 IF-MIB::ifHCOutUcastPkts
snmpwalk -v2c -c abc 10.213.0.17 IF-MIB::ifInDiscards
snmpwalk -v2c -c abc 10.213.0.17 IF-MIB::ifOutDiscards
