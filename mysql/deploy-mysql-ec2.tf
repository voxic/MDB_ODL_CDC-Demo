provider "aws" {
  region = "eu-north-1"
}

resource "aws_instance" "ec2" {
  count = 2
  ami = "ami-07bdb714a483cb3bc"
  instance_type = "t3.micro"
  key_name = "<your name>"
  vpc_security_group_ids = ["<your securitygroup>"]
  tags = {
    Name = "mysql",
    owner = "<your name>",
    expires-on = "<expires-on>",
    purpose = "<your purpose>"
  }

  user_data = <<EOF
    #!/bin/bash
    sudo yum update -y
    sudo amazon-linux-extras install docker
    sudo service docker start
    sudo docker run --name mysql -e MYSQL_ROOT_PASSWORD=MongoDB2022!test2023 -p 3306:3306 -d mysql
    EOF
}
