from curler.curler import curler as cl
import unittest2

class testCurler(unittest2.TestCase):
    def setUp(self):
        self.cl = cl()

    def atest_transfer(self):
        cert = ("--cert " +
                "/mnt/trSP-2788-olabs_kbrs/external/common/olabs-unknownhost-r2-anyAD/cert.pem:\"\" " +
                "--key " +
                "/mnt/transfer/certs/20180607-SP-2788-olabs_kbrs/external/common/olabs-unknownhost-r2-anyAD/dec.key")
        rest = " https://network-telemetry.ad1.r2.oracleiaas.com/prometheus/api/v1/query?query="
        query = "ifInErrors{device=~'phx3-svc1-tor3',interface='Ethernet11'}[20m]&time=1533688700"

        msg ="curl -s --globoff -k " + cert + "-X GET " + rest + query
        self.cl.msg(msg)

    def test_prometheus(self):

        cert = ""
        rest = "http://localhost:9090/api/v1/query?query="
        query = "{__name__=~[a-z].+}[1m]"
        msg = "curl -s --globoff -k " + cert + "-X GET " + rest + query
        outfile = "resources/prom.json"

        self.cl.msg = msg
        self.cl.outfile = outfile
        self.cl.send()


if __name__ == "__main__":
    unittest2.main()
