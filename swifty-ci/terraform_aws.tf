provider "aws" {}

data "aws_ami" "fedora" {
  most_recent = true

  filter {
    name   = "name"
    values = ["*Fedora-Cloud-Base-27*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["125523088429"]  # Fedora official images

}

resource "aws_security_group" "sec_group" {
  name        = "abcdef_sec_group"
  description = "Allow all inbound traffic"

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port       = 0
    to_port         = 0
    protocol        = "-1"
    cidr_blocks     = ["0.0.0.0/0"]
  }
}


resource "aws_instance" "gateway_abcdef" {
  ami           = "${data.aws_ami.fedora.id}"
  instance_type = "t2.medium"
  key_name      = "vgrevtsev"
  security_groups = ["${aws_security_group.sec_group.name}"]
  tags {
    Name = "swifty-gateway-abcdef"
    Commit = "abcdef"
  }
  root_block_device {
    volume_size = 20
  }
  depends_on = ["aws_security_group.sec_group"]
  provisioner "local-exec" {
    command = "aws ec2 wait instance-status-ok --instance-ids ${aws_instance.gateway_abcdef.id}"
  }
}


output "gateway::public_ip" {
  value = "${aws_instance.gateway_abcdef.public_ip}"
}

output "gateway::private_ip" {
  value = "${aws_instance.gateway_abcdef.private_ip}"
}

output "gateway::public_dns" {
  value = "${aws_instance.gateway_abcdef.public_dns}"
}



resource "aws_instance" "middleware_abcdef" {
  ami           = "${data.aws_ami.fedora.id}"
  instance_type = "t2.medium"
  key_name      = "vgrevtsev"
  security_groups = ["${aws_security_group.sec_group.name}"]
  tags {
    Name = "swifty-middleware-abcdef"
    Commit = "abcdef"
  }
  root_block_device {
    volume_size = 10
  }
  depends_on = ["aws_security_group.sec_group"]
  provisioner "local-exec" {
    command = "aws ec2 wait instance-status-ok --instance-ids ${aws_instance.middleware_abcdef.id}"
  }
}


output "middleware::public_ip" {
  value = "${aws_instance.middleware_abcdef.public_ip}"
}

output "middleware::private_ip" {
  value = "${aws_instance.middleware_abcdef.private_ip}"
}

output "middleware::public_dns" {
  value = "${aws_instance.middleware_abcdef.public_dns}"
}



resource "aws_instance" "dashboard_abcdef" {
  ami           = "${data.aws_ami.fedora.id}"
  instance_type = "t2.medium"
  key_name      = "vgrevtsev"
  security_groups = ["${aws_security_group.sec_group.name}"]
  tags {
    Name = "swifty-dashboard-abcdef"
    Commit = "abcdef"
  }
  root_block_device {
    volume_size = 10
  }
  depends_on = ["aws_security_group.sec_group"]
  provisioner "local-exec" {
    command = "aws ec2 wait instance-status-ok --instance-ids ${aws_instance.dashboard_abcdef.id}"
  }
}


output "dashboard::public_ip" {
  value = "${aws_instance.dashboard_abcdef.public_ip}"
}

output "dashboard::private_ip" {
  value = "${aws_instance.dashboard_abcdef.private_ip}"
}

output "dashboard::public_dns" {
  value = "${aws_instance.dashboard_abcdef.public_dns}"
}



resource "aws_instance" "worker0_abcdef" {
  ami           = "${data.aws_ami.fedora.id}"
  instance_type = "t2.medium"
  key_name      = "vgrevtsev"
  security_groups = ["${aws_security_group.sec_group.name}"]
  tags {
    Name = "swifty-worker0-abcdef"
    Commit = "abcdef"
  }
  root_block_device {
    volume_size = 10
  }
  depends_on = ["aws_security_group.sec_group"]
  provisioner "local-exec" {
    command = "aws ec2 wait instance-status-ok --instance-ids ${aws_instance.worker0_abcdef.id}"
  }
}


output "worker0::public_ip" {
  value = "${aws_instance.worker0_abcdef.public_ip}"
}

output "worker0::private_ip" {
  value = "${aws_instance.worker0_abcdef.private_ip}"
}

output "worker0::public_dns" {
  value = "${aws_instance.worker0_abcdef.public_dns}"
}



resource "aws_instance" "worker1_abcdef" {
  ami           = "${data.aws_ami.fedora.id}"
  instance_type = "t2.medium"
  key_name      = "vgrevtsev"
  security_groups = ["${aws_security_group.sec_group.name}"]
  tags {
    Name = "swifty-worker1-abcdef"
    Commit = "abcdef"

  }
  root_block_device {
    volume_size = 10
  }
  depends_on = ["aws_security_group.sec_group"]
  provisioner "local-exec" {
    command = "aws ec2 wait instance-status-ok --instance-ids ${aws_instance.worker1_abcdef.id}"
  }
}


output "worker1::public_ip" {
  value = "${aws_instance.worker1_abcdef.public_ip}"
}

output "worker1::private_ip" {
  value = "${aws_instance.worker1_abcdef.private_ip}"
}

output "worker1::public_dns" {
  value = "${aws_instance.worker1_abcdef.public_dns}"
}


