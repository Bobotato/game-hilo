resource "digitalocean_droplet" "hilo-game" {
  count = 3
  image = "ubuntu-20-04-x64"
  name = "hilo-game-${count.index}"
  region = "sgp1"
  size = "s-1vcpu-512mb-10gb"

  ssh_keys = [
    data.digitalocean_ssh_key.Alexvm.id
  ]

    connection {
    host = self.ipv4_address
    user = "root"
    type = "ssh"
    private_key = file(var.pvt_key)
    timeout = "2m"
  }

    provisioner "local-exec" {
        command = "ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -u root -i '${self.ipv4_address},' -e @/home/alex/Desktop/game-hilo/dockerhub_login.enc --vault-password-file /home/alex/Desktop/game-hilo/vault_pass.txt /home/alex/Desktop/game-hilo/playbook.yml"
    }
}

output "drop_ip_addresses" {
    value = {
        for droplet in digitalocean_droplet.hilo-game:
        droplet.name => droplet.ipv4_address
    }
    }
