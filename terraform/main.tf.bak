resource "digitalocean_droplet" "hilo-game" {
  count = 1
  image = "debian-11-x64"
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
    private_key = var.pvt_key
    timeout = "2m"
  }

    provisioner "local-exec" {
                command = "until nc -zv '${self.ipv4_address}' 22; do sleep 1; done; echo 'SSH port open' && export ANSIBLE_HOST_KEY_CHECKING=False && ansible-playbook -u root -i inventory --private-key '${var.pvt_key}' ../playbook.yml -vvvv"

    }
}

resource "local_file" "ansible_inventory" {
  content = templatefile("hosts.tftpl",
    {
    digitalocean_droplets = digitalocean_droplet.hilo-game.*.ipv4_address
    }
  )
  filename = "./inventory"
}

output "drop_ip_addresses" {
    value = {
        for droplet in digitalocean_droplet.hilo-game:
        droplet.name => droplet.ipv4_address
    }
}
