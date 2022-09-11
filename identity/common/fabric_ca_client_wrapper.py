import subprocess

from identity.base.support.utils import log_msg


class FabricCaClientWrapper:
    home = None
    address = None
    port = None
    caname = None
    tls_certfiles = None
    enrollment_id = None
    enrollment_secret = None

    def __init__(self, home: str,
                 address: str,
                 port: str,
                 caname: str,
                 tls_certfiles: str,
                 enrollment_id: str,
                 enrollment_secret: str):
        self.home = home
        self.address = address
        self.port = port
        self.caname = caname
        self.tls_certfiles = tls_certfiles
        self.enrollment_id = enrollment_id
        self.enrollment_secret = enrollment_secret

    def generate_url(self):
        return f"https://{self.enrollment_id}:{self.enrollment_secret}@{self.address}:{self.port}"

    def enroll(self):
        command_list = ["fabric-ca-client", "enroll",
                                       "-u", self.generate_url(),
                                       "--caname", self.caname,
                                       "--tls.certfiles", self.tls_certfiles,
                                       "--home", self.home]
        return_code = subprocess.call(command_list)
        log_msg(' '.join(command_list))
        if return_code == 0:
            log_msg("Enrolled successfully.")
        else:
            log_msg(f"Enrollment failed. Code: {return_code}")

    def enroll_msp(self, msp):
        command_list = ["fabric-ca-client", "enroll",
                        "-u", self.generate_url(),
                        "--caname", self.caname,
                        "--tls.certfiles", self.tls_certfiles,
                        "--home", self.home,
                        "--mspdir", msp]

        return_code = subprocess.call(command_list)
        log_msg(' '.join(command_list))
        if return_code == 0:
            log_msg("Enrolled successfully.")
        else:
            log_msg(f"Enrollment failed. Code: {return_code}")

    def register(self, id_name, id_secret, id_attrs):
        command_list = ["fabric-ca-client", "register",
                                       "--caname", self.caname,
                                       "--id.name", id_name,
                                       "--id.secret", id_secret,
                                       "--id.type", "client",
                                       "--id.attrs", id_attrs,
                                       "--tls.certfiles", self.tls_certfiles,
                                       "--home", self.home]
        log_msg(' '.join(command_list))
        return_code = subprocess.call(command_list)
        if return_code == 0:
            log_msg("Registered successfully.")
        else:
            log_msg(f"Registration failed. Code: {return_code}")

    def register_fl_admin(self, id_name, id_secret):
        self.register(id_name, id_secret, "'flAdmin=true:ecert'")

    def register_trainer(self, id_name, id_secret):
        self.register(id_name, id_secret, "trainer=true:ecert")

    def register_aggregator(self, id_name, id_secret):
        self.register(id_name, id_secret, "'aggregator=true:ecert'")

    def register_lead_aggregator(self, id_name, id_secret):
        self.register(id_name, id_secret, "'leadAggregator=true:ecert'")

