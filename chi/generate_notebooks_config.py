import chi


notebooks_config = { 'base_folder':'/home/pruth/work/working',
                     'groups' : [ {'name': 'Reservations', 'subfolder': 'reservations' },
                               {'name': 'Networking', 'subfolder': 'networking' },
                               {'name': 'Servers', 'subfolder': 'servers' },
                             ],
                 
                 
                 
                   'modules' : [ 
                       
                  # Reservation Modules     
                  { 'title':          'Reserve Node',
                    'function':       'reserve_node',
                    'related_modules':[ 'reserve_floating_ip', 'reserve_network', 'delete_lease' ],
                    'include_code':   [ 'add_node_reservation'],
                    'examples':       [ 'reserve_node_notebook'],
                    'notebook_file':  'reserve_node_notebook.ipynb',
                    'group':          'Reservations',
                  }, 
                 
                 { 'title':          'Reserve Floating IP',
                    'function':       'reserve_floating_ip',
                    'related_modules':[ 'reserve_node', 'reserve_network', 'delete_lease' ],
                    'include_code':   [ 'add_fip_reservation'],
                    'examples':       [ 'reserve_floating_ip_notebook'],
                    'notebook_file':  'reserve_floating_ip.ipynb',
                    'group':          'Reservations',
                 },
                 
                 { 'title':          'Reserve Network',
                    'function':       'reserve_network',
                    'related_modules':[ 'reserve_floating_ip', 'reserve_node', 'delete_lease' ],
                    'include_code':   [ 'add_network_reservation'],
                    'examples':       [ 'reserve_network_notebook'],
                    'notebook_file':  'reserve_network.ipynb',
                    'group':          'Reservations',
                 },
                 
                 { 'title':          'Delete Lease',
                    'function':       'delete_lease_by_name',
                    'related_modules':[ 'reserve_node' ],
                    'include_code':   [ 'delete_lease_by_id' ],
                    'examples':       [ 'delete_lease_notebook'],
                    'notebook_file':  'delete_lease.ipynb',
                    'group':          'Reservations',
                 },
                 
                 { 'title':          'Reserve Multiple Resources',
                    'function':       'reserve_multiple_resources',
                    'related_modules':[ ],
                    'include_code':   ['add_node_reservation', 'add_network_reservation', 'add_fip_reservation'],
                    'examples':       [ ],
                    'notebook_file':  'reserve_multiple_resources.ipynb',
                    'group':          'Reservations',
                 },
                 { 'title':          'Get Lease',
                    'function':       'get_lease_by_name',
                    'related_modules':[ ],
                    'include_code':   [ ],
                    'examples':       [ ],
                    'notebook_file':  'get_lease.ipynb',
                    'group':          'Reservations',
                 },
                 { 'title':          'Get Reservation',
                    'function':       'get_lease_by_name',
                    'related_modules':[ ],
                    'include_code':   [ ],
                    'examples':       [ ],
                    'notebook_file':  'get_reservation.ipynb',
                    'group':          'Reservations',
                 },
                  
                                
                 #Server Modules       
                 { 'title':          'Create Server',
                    'function':       'create_server',
                    'related_modules':[  ],
                    'include_code':   [  ],
                    'examples':       [  ],
                    'notebook_file':  'create_server.ipynb',
                    'group':          'Servers',
                 },
                   { 'title':          'Delete Server',
                    'function':       'delete_server',
                    'related_modules':[ ],
                    'include_code':   [ 'delete_server_by_name' ],
                    'examples':       [ ],
                    'notebook_file':  'delete_server.ipynb',
                    'group':          'Servers',
                 },
                   { 'title':          'Associate Floating IP',
                    'function':       'associate_floating_ip',
                    'related_modules':[ ],
                    'include_code':   [ ],
                    'examples':       [ ],
                    'notebook_file':  'associate_floating_ip.ipynb',
                    'group':          'Servers',
                 },
                   { 'title':          'Detach Floating IP',
                    'function':       'detach_floating_ip',
                    'related_modules':[ ],
                    'include_code':   [ ],
                    'examples':       [ ],
                    'notebook_file':  'detach_floating_ip.ipynb',
                    'group':          'Servers',
                 },
                                
                 
                #Networking Modules
                { 'title':          'Add Subnet',
                    'function':       'add_subnet',
                    'related_modules':[ ],
                    'include_code':   [ 'get_network_by_name'],
                    'examples':       [ ],
                    'notebook_file':  'add_subnet.ipynb',
                    'group':          'Networking',
                 },
                { 'title':          'Create Router',
                    'function':       'create_router',
                    'related_modules':[ 'create_network', 'delete_router_by_name' ],
                    'include_code':   [ ],
                    'examples':       [ 'create_router_notebook' ],
                    'notebook_file':  'create_router.ipynb',
                    'group':          'Networking',
                 },
                { 'title':          'Create Network',
                    'function':       'create_network',
                    'related_modules':[ ],
                    'include_code':   [ ],
                    'examples':       [ 'create_network_notebook' ],
                    'notebook_file':  'create_network.ipynb',
                    'group':          'Networking',
                 },
                { 'title':          'Delete Network',
                    'function':       'delete_network_by_name',
                    'related_modules':[ ],
                    'include_code':   [ 'get_network_by_name' ],
                    'examples':       [ ],
                    'notebook_file':  'delete_network_by_name.ipynb',
                    'group':          'Networking',
                 },
                { 'title':          'Delete Subnet',
                    'function':       'delete_subnet_by_name',
                    'related_modules':[ 'delete_subnet_by_id', 'get_subnet_by_name'],
                    'include_code':   [ ],
                    'examples':       [ ],
                    'notebook_file':  'delete_subnet_by_name.ipynb',
                    'group':          'Networking',
                 },
                { 'title':          'Delete Router',
                    'function':       'delete_router_by_name',
                    'related_modules':[ ],
                    'include_code':   [ ],
                    'examples':       [ ],
                    'notebook_file':  'delete_router_by_name.ipynb',
                    'group':          'Networking',
                 },
                { 'title':          'Attach Router',
                    'function':       'attach_router_to_subnet',
                    'related_modules':[ ],
                    'include_code':   [ ],
                    'examples':       [ ],
                    'notebook_file':  'attach_router_to_subnet.ipynb',
                    'group':          'Networking',
                 },
                { 'title':          'Detach Router',
                    'function':       'detach_router_by_name',
                    'related_modules':[ ],
                    'include_code':   [ 'detach_router_by_id' ],
                    'examples':       [ ],
                    'notebook_file':  '.ipynb',
                    'group':          'Networking',
                 },
                { 'title':          'Get Network by Name',
                    'function':       'get_network_by_name',
                    'related_modules':[ ],
                    'include_code':   [ ],
                    'examples':       [ ],
                    'notebook_file':  'get_network_by_name.ipynb',
                    'group':          'Networking',
                 },
                { 'title':          'Get Subnet by Name',
                    'function':       'get_subnet_by_name',
                    'related_modules':[ ],
                    'include_code':   [ ],
                    'examples':       [ ],
                    'notebook_file':  'get_subnet_by_name.ipynb',
                    'group':          'Networking',
                 },
                { 'title':          'Get Router by Name',
                    'function':       'get_router_by_name',
                    'related_modules':[ ],
                    'include_code':   [ ],
                    'examples':       [ ],
                    'notebook_file':  'get_router_by_name.ipynb',
                    'group':          'Networking',
                 },

                       
#                { 'title':          'Get Network Property',
#                    'function':       'get_network_property',
#                    'related_modules':[ ],
#                    'include_code':   [ ],
#                    'examples':       [ ],
#                    'notebook_file':  'get_network_property.ipynb',
#                    'group':          'Networking',
#                 },
#                { 'title':          'Get Subnet Property',
#                    'function':       'get_subnet_property',
#                    'related_modules':[ ],
#                    'include_code':   [ ],
#                    'examples':       [ ],
#                    'notebook_file':  'get_subnet_property.ipynb',
#                    'group':          'Networking',
#                 },
#                { 'title':          'Get Router Property',
#                    'function':       'get_router_property',
#                    'related_modules':[ ],
#                    'include_code':   [ ],
#                    'examples':       [ ],
#                    'notebook_file':  'get_router_property.ipynb',
#                    'group':          'Networking',
#                 },
#                { 'title':          'ExoGENI Stitching',
#                    'function':       'exogeni_stitching',
#                    'related_modules':[ ],
#                    'include_code':   [ ],
#                    'examples':       [ ],
#                    'notebook_file':  'exogeni_stitching.ipynb',
#                    'group':          'Networking',
#                 },
                            
                ],
                 

                'tutorials' : [ { 'title':          'Isolated Network VLANs', 
                                  'path':       '../tutorials-python/IsolatedNetworks.ipynb',
                                },
                                { 'title':          'Network Stitching (ExoGENI)', 
                                  'path':       '../tutorials-python/NetworkStitching.ipynb',
                                },
                              ]    
                   
                }
                              