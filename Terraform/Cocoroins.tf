data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}

resource "aws_instance" "Cocoroins" {
  ami           = "ami-0e83be366243f524a"
  instance_type = "t2.micro"
  key_name = "Demo"
  security_groups = [aws_security_group.allow_http-ssh.id]
  subnet_id = "subnet-0deb9639bf53021ad"

  tags = {
    Name = "Cocoroins"
  }
}

output "My_ip"{
  value = aws_instance.Cocoroins.public_ip
}

resource "aws_security_group" "allow_http-ssh" {
  name        = "allow_HTTP-SSH"
  description = "Allow HTTP-SSH inbound traffic"
  vpc_id      = "vpc-0566bcb19fdb8b82d"

  ingress {
    description      = "HTTP from VPC"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

 ingress {
    description      = "SSH from VPC"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

 ingress {
    description      = "Webgoat from VPC"
    from_port        = 8080
    to_port          = 8080
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

 egress {
   from_port         = 0
   to_port           = 0
   protocol          = "-1"
   cidr_blocks       = ["0.0.0.0/0"]
 }

  tags = {
    Name = "allow_HTTP-SSH"
  }
}
