import chi
import json
import os

from chi.reservation_api_examples import *
from chi.networking_api_examples import *

#nova = chi.nova()
#blazar = chi.blazar()
#neutron = chi.neutron()
#glance = chi.glance()

def get_image_by_name(name):
    try:
        return chi.glance().images.get(image_id=name)
    except:
        images = list(chi.glance().images.list(filters={'name': name}))
        if len(images) < 1:
            raise RuntimeError('no images found matching name or ID "{}"'.format(name))
        elif len(images) > 1:
            raise RuntimeError('multiple images found matching name "{}"'.format(name))
        else:
            return images[0]

def get_flavor_by_name(name):
    flavor = next((f for f in chi.nova().flavors.list() if f.name == name), None)

    if not flavor:
        raise RuntimeError('no flavor found matching name "{}"'.format(name))
    
    return flavor
    

def get_server_by_name(name):
    server = None    
    for s in chi.nova().servers.list():
        if s.name == name:
            if server == None:
                server = s
            else:
                print("Found multiple servers with name " + str(name))
                return None
    return server

def get_free_floating_ip():
    '''Gets or creates a free floating IP to use'''
    ips = chi.neutron().list_floatingips()['floatingips']
    print (ips)
    unbound = (ip for ip in ips if ip['port_id'] is None)
    try:
        fip = next(unbound)
        return fip
    except StopIteration:
        print("No free floating IP found")


def associate_floating_ip(server_name, floating_ip_str=None):
    server = get_server_by_name(server_name)
    
    if floating_ip_str == None:
        fip = get_free_floating_ip()
    else:
        fip = get_specific_floating_ip(floating_ip_str)
  
    if fip == None:
        return
    ip = fip['floating_ip_address']
    
    # using method from https://github.com/ChameleonCloud/horizon/blob/f5cf987633271518970b24de4439e8c1f343cad9/openstack_dashboard/api/neutron.py#L518
    ports = chi.neutron().list_ports(**{'device_id': server.id}).get('ports')
    fip_target = {
        'port_id': ports[0]['id'],
        'ip_addr': ports[0]['fixed_ips'][0]['ip_address']
    }
    # https://github.com/ChameleonCloud/horizon/blob/f5cf987633271518970b24de4439e8c1f343cad9/openstack_dashboard/dashboards/project/instances/tables.py#L671
    target_id = fip_target['port_id']
    chi.neutron().update_floatingip(fip['id'], body={
             'floatingip': {
                 'port_id': target_id,
                 # 'fixed_ip_address': ip_address,
              }
          }
    )
    return ip

def get_specific_floating_ip(ip_str):
    ips = chi.neutron().list_floatingips()['floatingips']
    
    for fip in ips:
        if fip['floating_ip_address'] == ip_str:
            return fip
    print("Floating ip not found " + ip_str)
    
    return None

def create_server(server_name, reservation_id, key_name, network_name='sharednet1', count=1, image_name='CC-CentOS7', flavor_name='baremetal'):
    # Get flavor
    flavor = get_flavor_by_name(name=flavor_name)
    
    #Get image
    image = get_image_by_name(name=image_name)
   
    #Get network
    network = get_network_by_name(name=network_name)
    network_id = network['id']
   
    server = chi.nova().servers.create(name=server_name,
                       image=image,
                       flavor=flavor,
                       scheduler_hints={'reservation': reservation_id},
                       key_name=key_name,
                       nics=[{"net-id": network_id, "v4-fixed-ip": ""}],
                       min_count=count,
                       max_count=count 
                       )
    return server
    
def delete_server_by_name(server_name):
    server = get_server_by_name(server_name)
    return server.delete()
    
def delete_server(server):
    return server.delete()

def detach_floating_ip(server_name, floating_ip_str):
    server = get_server_by_name(server_name)
    fip = get_specific_floating_ip(ip_str)
    
    chi.neutron().update_floatingip(floating_ip['id'],
                {'floatingip': {'port_id': None}})