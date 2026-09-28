# Inital Recon

## Preexisiting creds

**Username** : contractor 
**Password** Contractor2026!

## Nmap scan 
the initial nmap scan reveals the 2 ports in the nmap scan
which is
* SSH port
* RDP port


## Recon in the device RDP


### opened ports

```
Netid State  Recv-Q Send-Q                   Local Address:Port    Peer Address:Port                                  Process                                   
udp   UNCONN 0      0                              0.0.0.0:5353         0.0.0.0:*                                                                               
udp   UNCONN 0      0                              0.0.0.0:56891        0.0.0.0:*                                                                               
udp   UNCONN 0      0                           127.0.0.54:53           0.0.0.0:*                                                                               
udp   UNCONN 0      0                        127.0.0.53%lo:53           0.0.0.0:*                                                                               
udp   UNCONN 0      0                   10.159.143.45%eth0:68           0.0.0.0:*                                                                               
udp   UNCONN 0      0                                 [::]:5353            [::]:*                                                                               
udp   UNCONN 0      0                                 [::]:59889           [::]:*                                                                               
udp   UNCONN 0      0      [fe80::216:3eff:fe83:ea41]%eth0:546             [::]:*                                                                               
tcp   LISTEN 0      4096                        127.0.0.54:53           0.0.0.0:*                                                                               
tcp   LISTEN 0      4096                           0.0.0.0:22           0.0.0.0:*                                                                               
tcp   LISTEN 0      4096                     127.0.0.53%lo:53           0.0.0.0:*                                                                               
tcp   LISTEN 0      4096                              [::]:22              [::]:*                                                                               
tcp   LISTEN 0      2                                [::1]:3350            [::]:*                                                                               
tcp   LISTEN 0      2                                    *:3389               *:*                                                       
```


## Running services
```
  UNIT                     LOAD   ACTIVE SUB     DESCRIPTION                   >
  accounts-daemon.service  loaded active running Accounts Service
  avahi-daemon.service     loaded active running Avahi mDNS/DNS-SD Stack
  console-getty.service    loaded active running Console Getty
  cron.service             loaded active running Regular background program pro>
  dbus.service             loaded active running D-Bus System Message Bus
● NetworkManager.service   masked active running NetworkManager.service
  polkit.service           loaded active running Authorization Manager
  rsyslog.service          loaded active running System Logging Service
  rtkit-daemon.service     loaded active running RealtimeKit Scheduling Policy >
  systemd-journald.service loaded active running Journal Service
  systemd-logind.service   loaded active running User Login Management
  systemd-networkd.service loaded active running Network Configuration
  systemd-resolved.service loaded active running Network Name Resolution
  systemd-udevd.service    loaded active running Rule-based Manager for Device >
  udisks2.service          loaded active running Disk Manager
  upower.service           loaded active running Daemon for power management
  user@1001.service        loaded active running User Manager for UID 1001
  wpa_supplicant.service   loaded active running WPA supplicant
  xrdp-sesman.service      loaded active running xrdp session manager
  xrdp.service             loaded active running xrdp daemon


```


## ip configs
```
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.159.143.45  netmask 255.255.255.0  broadcast 10.159.143.255
        inet6 fd42:3ff5:6554:20e5:216:3eff:fe83:ea41  prefixlen 64  scopeid 0x0<global>
        inet6 fe80::216:3eff:fe83:ea41  prefixlen 64  scopeid 0x20<link>
        ether 00:16:3e:83:ea:41  txqueuelen 1000  (Ethernet)
        RX packets 80  bytes 9292 (9.2 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 149  bytes 15960 (15.9 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 5516  bytes 8902978 (8.9 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 5516  bytes 8902978 (8.9 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlan2: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether 02:00:00:00:02:00  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlan3: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether 02:00:00:00:03:00  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0


```



## Netstat
```
Proto RefCnt Flags       Type       State         I-Node   Path
unix  3      [ ]         STREAM     CONNECTED     36541    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     67715    /run/user/1001/at-spi/bus_10.0
unix  3      [ ]         STREAM     CONNECTED     70816    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     62598    
unix  3      [ ]         STREAM     CONNECTED     60263    
unix  3      [ ]         STREAM     CONNECTED     57874    @/tmp/.X11-unix/X10
unix  3      [ ]         DGRAM      CONNECTED     54718    
unix  3      [ ]         STREAM     CONNECTED     62035    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     35624    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     67182    
unix  3      [ ]         STREAM     CONNECTED     57873    
unix  3      [ ]         STREAM     CONNECTED     60175    
unix  3      [ ]         STREAM     CONNECTED     32150    
unix  3      [ ]         STREAM     CONNECTED     69309    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     67745    
unix  3      [ ]         STREAM     CONNECTED     198051   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     55583    /run/user/1001/bus
unix  2      [ ]         DGRAM      CONNECTED     33200    
unix  3      [ ]         STREAM     CONNECTED     35622    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     56374    
unix  3      [ ]         STREAM     CONNECTED     59383    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     60177    @/tmp/.X11-unix/X10
unix  3      [ ]         DGRAM      CONNECTED     54719    
unix  3      [ ]         STREAM     CONNECTED     38387    
unix  3      [ ]         STREAM     CONNECTED     37179    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     69311    
unix  3      [ ]         STREAM     CONNECTED     57110    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     55849    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     33212    
unix  3      [ ]         STREAM     CONNECTED     57220    
unix  3      [ ]         STREAM     CONNECTED     212556   
unix  3      [ ]         STREAM     CONNECTED     40119    
unix  3      [ ]         STREAM     CONNECTED     200190   
unix  3      [ ]         STREAM     CONNECTED     62512    
unix  3      [ ]         STREAM     CONNECTED     56955    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     32521    
unix  2      [ ]         DGRAM      CONNECTED     36436    
unix  3      [ ]         STREAM     CONNECTED     56916    
unix  3      [ ]         STREAM     CONNECTED     67657    /run/user/1001/at-spi/bus_10.0
unix  3      [ ]         STREAM     CONNECTED     36650    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     211956   /home/contractor/.cache/ibus/dbus-hjg5LE2i
unix  3      [ ]         STREAM     CONNECTED     62513    
unix  2      [ ]         DGRAM                    52781    /run/user/1001/systemd/notify
unix  3      [ ]         STREAM     CONNECTED     36422    /run/systemd/journal/stdout
unix  2      [ ]         DGRAM      CONNECTED     197990   
unix  3      [ ]         STREAM     CONNECTED     57221    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     32202    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     67743    
unix  3      [ ]         STREAM     CONNECTED     60264    
unix  3      [ ]         STREAM     CONNECTED     69308    
unix  3      [ ]         STREAM     CONNECTED     33208    
unix  3      [ ]         STREAM     CONNECTED     60265    
unix  3      [ ]         STREAM     CONNECTED     69904    /run/dbus/system_bus_socket
unix  3      [ ]         DGRAM      CONNECTED     17731    /run/systemd/notify
unix  3      [ ]         STREAM     CONNECTED     33207    
unix  3      [ ]         STREAM     CONNECTED     57109    
unix  3      [ ]         STREAM     CONNECTED     213164   
unix  3      [ ]         STREAM     CONNECTED     37387    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     67690    
unix  3      [ ]         STREAM     CONNECTED     58102    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     37172    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     36421    
unix  3      [ ]         STREAM     CONNECTED     32201    
unix  3      [ ]         STREAM     CONNECTED     58330    /home/contractor/.cache/ibus/dbus-hjg5LE2i
unix  2      [ ]         DGRAM      CONNECTED     32537    
unix  2      [ ]         DGRAM                    17754    /run/systemd/journal/syslog
unix  2      [ ]         DGRAM      CONNECTED     19352    
unix  16     [ ]         DGRAM      CONNECTED     19559    /run/systemd/journal/dev-log
unix  3      [ ]         STREAM     CONNECTED     58284    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     57919    @/tmp/.X11-unix/X10
unix  8      [ ]         DGRAM      CONNECTED     19562    /run/systemd/journal/socket
unix  3      [ ]         STREAM     CONNECTED     67622    
unix  2      [ ]         DGRAM      CONNECTED     37166    
unix  3      [ ]         DGRAM      CONNECTED     31095    
unix  3      [ ]         STREAM     CONNECTED     57334    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     33137    
unix  3      [ ]         STREAM     CONNECTED     63979    
unix  3      [ ]         STREAM     CONNECTED     57070    
unix  3      [ ]         STREAM     CONNECTED     67269    
unix  3      [ ]         STREAM     CONNECTED     56707    /run/user/1001/bus
unix  3      [ ]         DGRAM      CONNECTED     31093    
unix  3      [ ]         STREAM     CONNECTED     60418    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     58288    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     63874    
unix  3      [ ]         DGRAM      CONNECTED     31096    
unix  3      [ ]         STREAM     CONNECTED     66147    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     60332    
unix  3      [ ]         STREAM     CONNECTED     57055    
unix  2      [ ]         DGRAM      CONNECTED     17777    
unix  3      [ ]         STREAM     CONNECTED     37167    
unix  2      [ ]         DGRAM      CONNECTED     31084    
unix  3      [ ]         STREAM     CONNECTED     68707    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     58277    /run/user/1001/at-spi/bus_10.0
unix  3      [ ]         STREAM     CONNECTED     61620    /home/contractor/.cache/ibus/dbus-hjg5LE2i
unix  3      [ ]         STREAM     CONNECTED     60420    
unix  3      [ ]         STREAM     CONNECTED     198820   
unix  3      [ ]         STREAM     CONNECTED     37168    
unix  2      [ ]         DGRAM                    63504    
unix  3      [ ]         STREAM     CONNECTED     63473    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     58326    /home/contractor/.cache/ibus/dbus-hjg5LE2i
unix  3      [ ]         STREAM     CONNECTED     60330    
unix  3      [ ]         STREAM     CONNECTED     213345   
unix  3      [ ]         STREAM     CONNECTED     63434    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     60338    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     58278    /run/user/1001/at-spi/bus_10.0
unix  3      [ ]         STREAM     CONNECTED     213159   
unix  3      [ ]         STREAM     CONNECTED     63381    @/tmp/.ICE-unix/664
unix  3      [ ]         STREAM     CONNECTED     37761    
unix  3      [ ]         STREAM     CONNECTED     60417    
unix  3      [ ]         STREAM     CONNECTED     57078    
unix  3      [ ]         STREAM     CONNECTED     198823   @/tmp/.X11-unix/X10
unix  3      [ ]         STREAM     CONNECTED     57879    /home/contractor/.cache/ibus/dbus-hjg5LE2i
unix  3      [ ]         STREAM     CONNECTED     70036    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     63500    
unix  3      [ ]         STREAM     CONNECTED     31065    
unix  3      [ ]         STREAM     CONNECTED     67628    
unix  3      [ ]         STREAM     CONNECTED     60452    
unix  3      [ ]         DGRAM      CONNECTED     17733    
unix  3      [ ]         STREAM     CONNECTED     56912    
unix  2      [ ]         DGRAM                    37760    
unix  3      [ ]         DGRAM      CONNECTED     31094    
unix  3      [ ]         STREAM     CONNECTED     58279    /run/user/1001/at-spi/bus_10.0
unix  3      [ ]         STREAM     CONNECTED     67804    
unix  3      [ ]         STREAM     CONNECTED     64007    
unix  3      [ ]         STREAM     CONNECTED     52786    /run/dbus/system_bus_socket
unix  3      [ ]         DGRAM      CONNECTED     33120    
unix  3      [ ]         STREAM     CONNECTED     67930    /run/user/1001/bus
unix  3      [ ]         DGRAM      CONNECTED     33121    
unix  3      [ ]         STREAM     CONNECTED     60421    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     68706    
unix  3      [ ]         STREAM     CONNECTED     57058    
unix  3      [ ]         STREAM     CONNECTED     70812    
unix  3      [ ]         STREAM     CONNECTED     37318    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     68704    
unix  3      [ ]         STREAM     CONNECTED     63495    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     60331    
unix  3      [ ]         STREAM     CONNECTED     56954    
unix  3      [ ]         STREAM     CONNECTED     56706    
unix  2      [ ]         DGRAM      CONNECTED     213327   
unix  3      [ ]         STREAM     CONNECTED     66730    @/tmp/.X11-unix/X10
unix  3      [ ]         STREAM     CONNECTED     60446    
unix  3      [ ]         STREAM     CONNECTED     56972    
unix  3      [ ]         STREAM     CONNECTED     31811    /run/systemd/journal/stdout
unix  3      [ ]         DGRAM      CONNECTED     17732    
unix  3      [ ]         STREAM     CONNECTED     37540    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     67204    @/tmp/.X11-unix/X10
unix  3      [ ]         STREAM     CONNECTED     60447    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     58103    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     35604    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     32230    
unix  3      [ ]         STREAM     CONNECTED     70000    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     213346   
unix  3      [ ]         STREAM     CONNECTED     56973    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     33175    
unix  3      [ ]         STREAM     CONNECTED     63974    
unix  3      [ ]         STREAM     CONNECTED     60329    
unix  3      [ ]         STREAM     CONNECTED     212550   @/tmp/.X11-unix/X10
unix  3      [ ]         STREAM     CONNECTED     63429    /run/user/1001/at-spi/bus_10.0
unix  3      [ ]         STREAM     CONNECTED     58280    /run/user/1001/at-spi/bus_10.0
unix  3      [ ]         STREAM     CONNECTED     57081    
unix  3      [ ]         STREAM     CONNECTED     36827    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     200072   
unix  3      [ ]         STREAM     CONNECTED     68699    
unix  3      [ ]         STREAM     CONNECTED     67606    /run/user/1001/at-spi/bus_10.0
unix  3      [ ]         STREAM     CONNECTED     53612    /run/systemd/journal/stdout
unix  2      [ ]         DGRAM      CONNECTED     32261    
unix  3      [ ]         STREAM     CONNECTED     68565    
unix  3      [ ]         STREAM     CONNECTED     61789    
unix  3      [ ]         STREAM     CONNECTED     58347    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     70032    
unix  3      [ ]         STREAM     CONNECTED     55353    
unix  3      [ ]         STREAM     CONNECTED     37479    
unix  3      [ ]         STREAM     CONNECTED     68710    
unix  3      [ ]         STREAM     CONNECTED     198050   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     62276    @/tmp/.X11-unix/X10
unix  3      [ ]         STREAM     CONNECTED     22392    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     58100    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     37539    
unix  3      [ ]         STREAM     CONNECTED     60472    
unix  3      [ ]         STREAM     CONNECTED     67197    @/tmp/.X11-unix/X10
unix  3      [ ]         STREAM     CONNECTED     61772    
unix  3      [ ]         STREAM     CONNECTED     37173    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     57803    
unix  3      [ ]         STREAM     CONNECTED     68652    
unix  3      [ ]         STREAM     CONNECTED     66285    @/tmp/.ICE-unix/664
unix  3      [ ]         STREAM     CONNECTED     69369    /run/user/1001/pulse/native
unix  3      [ ]         STREAM     CONNECTED     60473    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     58940    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     70007    
unix  3      [ ]         STREAM     CONNECTED     68563    
unix  3      [ ]         STREAM     CONNECTED     66319    @/tmp/.X11-unix/X10
unix  3      [ ]         STREAM     CONNECTED     58346    
unix  2      [ ]         DGRAM      CONNECTED     37537    
unix  3      [ ]         STREAM     CONNECTED     59389    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     53231    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     69368    @/tmp/.X11-unix/X10
unix  3      [ ]         STREAM     CONNECTED     61826    
unix  3      [ ]         STREAM     CONNECTED     59097    @/tmp/.X11-unix/X10
unix  3      [ ]         STREAM     CONNECTED     58905    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     67701    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     57843    
unix  3      [ ]         STREAM     CONNECTED     21203    
unix  3      [ ]         STREAM     CONNECTED     197989   /run/xrdp/sockdir/xrdp_chansrv_socket_10
unix  3      [ ]         STREAM     CONNECTED     67178    @/tmp/.ICE-unix/664
unix  3      [ ]         STREAM     CONNECTED     70023    @/tmp/.X11-unix/X10
unix  2      [ ]         DGRAM                    40934    /run/wpa_supplicant/wlan2
unix  3      [ ]         STREAM     CONNECTED     59390    
unix  3      [ ]         STREAM     CONNECTED     52080    
unix  2      [ ]         DGRAM                    40954    /run/wpa_supplicant/p2p-dev-wlan2
unix  3      [ ]         STREAM     CONNECTED     67237    
unix  3      [ ]         STREAM     CONNECTED     60518    
unix  2      [ ]         DGRAM                    47110    /run/wpa_supplicant/wlan3
unix  3      [ ]         STREAM     CONNECTED     61771    
unix  3      [ ]         STREAM     CONNECTED     70022    
unix  3      [ ]         STREAM     CONNECTED     67936    
unix  3      [ ]         STREAM     CONNECTED     61769    
unix  3      [ ]         STREAM     CONNECTED     37180    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     69048    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     54630    /run/systemd/journal/stdout
unix  2      [ ]         DGRAM      CONNECTED     21249    
unix  3      [ ]         STREAM     CONNECTED     68690    
unix  3      [ ]         STREAM     CONNECTED     200073   /run/xrdp/sockdir/xrdp_display_10
unix  3      [ ]         STREAM     CONNECTED     62012    
unix  3      [ ]         STREAM     CONNECTED     70031    
unix  3      [ ]         STREAM     CONNECTED     57826    
unix  2      [ ]         DGRAM      CONNECTED     37669    
unix  3      [ ]         STREAM     CONNECTED     62013    @/tmp/.ICE-unix/664
unix  3      [ ]         STREAM     CONNECTED     67729    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     68977    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     55461    
unix  2      [ ]         DGRAM      CONNECTED     37748    
unix  3      [ ]         STREAM     CONNECTED     58341    /run/user/1001/at-spi/bus_10.0
unix  3      [ ]         STREAM     CONNECTED     66578    @/tmp/.X11-unix/X10
unix  3      [ ]         STREAM     CONNECTED     58340    
unix  3      [ ]         STREAM     CONNECTED     70814    /run/user/1001/gvfsd/socket-eK7ibePO
unix  3      [ ]         STREAM     CONNECTED     37481    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     200189   
unix  3      [ ]         STREAM     CONNECTED     58342    
unix  3      [ ]         STREAM     CONNECTED     62072    
unix  3      [ ]         STREAM     CONNECTED     60519    @/tmp/.X11-unix/X10
unix  3      [ ]         STREAM     CONNECTED     67786    /run/user/1001/at-spi/bus_10.0
unix  3      [ ]         STREAM     CONNECTED     200076   
unix  3      [ ]         STREAM     CONNECTED     66101    @/tmp/.ICE-unix/664
unix  3      [ ]         STREAM     CONNECTED     59384    
unix  2      [ ]         DGRAM      CONNECTED     38592    
unix  3      [ ]         STREAM     CONNECTED     212554   /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     56915    
unix  3      [ ]         STREAM     CONNECTED     35960    
unix  3      [ ]         STREAM     CONNECTED     69072    
unix  3      [ ]         STREAM     CONNECTED     66333    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     58299    /home/contractor/.cache/ibus/dbus-hjg5LE2i
unix  3      [ ]         STREAM     CONNECTED     70019    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     67728    /run/user/1001/at-spi/bus_10.0
unix  3      [ ]         STREAM     CONNECTED     58292    
unix  3      [ ]         STREAM     CONNECTED     213163   
unix  3      [ ]         STREAM     CONNECTED     67783    
unix  3      [ ]         STREAM     CONNECTED     65971    @/tmp/.ICE-unix/664
unix  3      [ ]         STREAM     CONNECTED     32203    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     61560    /run/user/1001/at-spi/bus_10.0
unix  3      [ ]         STREAM     CONNECTED     69847    
unix  3      [ ]         STREAM     CONNECTED     66334    
unix  3      [ ]         STREAM     CONNECTED     56911    /home/contractor/.cache/ibus/dbus-hjg5LE2i
unix  3      [ ]         STREAM     CONNECTED     69019    
unix  3      [ ]         STREAM     CONNECTED     60676    
unix  3      [ ]         STREAM     CONNECTED     62630    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     58274    
unix  3      [ ]         STREAM     CONNECTED     57897    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     59342    
unix  3      [ ]         STREAM     CONNECTED     67727    /run/user/1001/at-spi/bus_10.0
unix  3      [ ]         STREAM     CONNECTED     67735    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     67734    /run/user/1001/at-spi/bus_10.0
unix  3      [ ]         STREAM     CONNECTED     67154    @/tmp/.X11-unix/X10
unix  2      [ ]         DGRAM      CONNECTED     214596   
unix  3      [ ]         STREAM     CONNECTED     58234    /run/user/1001/bus
unix  2      [ ]         DGRAM      CONNECTED     52718    
unix  3      [ ]         STREAM     CONNECTED     70703    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     69858    
unix  3      [ ]         STREAM     CONNECTED     60524    
unix  3      [ ]         STREAM     CONNECTED     53839    
unix  3      [ ]         STREAM     CONNECTED     56716    /run/systemd/journal/stdout
unix  2      [ ]         DGRAM      CONNECTED     53838    
unix  3      [ ]         DGRAM      CONNECTED     52782    
unix  3      [ ]         STREAM     CONNECTED     62090    
unix  3      [ ]         STREAM     CONNECTED     211954   /run/user/1001/at-spi/bus_10.0
unix  3      [ ]         STREAM     CONNECTED     69058    
unix  3      [ ]         STREAM     CONNECTED     67679    /run/user/1001/at-spi/bus_10.0
unix  3      [ ]         STREAM     CONNECTED     65404    
unix  3      [ ]         STREAM     CONNECTED     58866    
unix  2      [ ]         DGRAM                    53229    /run/xrdp/sockdir/xrdp_disconnect_display_10
unix  2      [ ]         DGRAM      CONNECTED     52742    
unix  2      [ ]         DGRAM                    35976    
unix  3      [ ]         STREAM     CONNECTED     66331    
unix  3      [ ]         STREAM     CONNECTED     69954    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     68736    
unix  3      [ ]         STREAM     CONNECTED     65359    
unix  3      [ ]         STREAM     CONNECTED     58275    
unix  3      [ ]         STREAM     CONNECTED     57849    
unix  3      [ ]         DGRAM      CONNECTED     20089    
unix  3      [ ]         STREAM     CONNECTED     60525    @/tmp/.X11-unix/X10
unix  3      [ ]         STREAM     CONNECTED     67746    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     67742    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     197200   
unix  3      [ ]         STREAM     CONNECTED     67235    
unix  3      [ ]         STREAM     CONNECTED     66335    @/tmp/.X11-unix/X10
unix  3      [ ]         STREAM     CONNECTED     61530    /run/user/1001/at-spi/bus_10.0
unix  3      [ ]         STREAM     CONNECTED     57889    @/tmp/.X11-unix/X10
unix  3      [ ]         STREAM     CONNECTED     59387    
unix  3      [ ]         STREAM     CONNECTED     66513    
unix  3      [ ]         STREAM     CONNECTED     61700    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     56910    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     69074    
unix  3      [ ]         STREAM     CONNECTED     67731    /run/user/1001/at-spi/bus_10.0
unix  3      [ ]         STREAM     CONNECTED     67656    
unix  3      [ ]         STREAM     CONNECTED     51819    /run/systemd/journal/stdout
unix  2      [ ]         DGRAM      CONNECTED     20085    
unix  3      [ ]         STREAM     CONNECTED     69075    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     68757    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     65965    
unix  3      [ ]         STREAM     CONNECTED     65643    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     63494    
unix  2      [ ]         DGRAM                    59314    
unix  3      [ ]         STREAM     CONNECTED     56914    
unix  3      [ ]         STREAM     CONNECTED     67732    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     69852    
unix  3      [ ]         STREAM     CONNECTED     63414    
unix  3      [ ]         STREAM     CONNECTED     62648    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     68840    
unix  3      [ ]         STREAM     CONNECTED     57844    
unix  3      [ ]         STREAM     CONNECTED     55323    /run/dbus/system_bus_socket
unix  3      [ ]         DGRAM      CONNECTED     52783    
unix  3      [ ]         STREAM     CONNECTED     22268    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     200211   /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     70038    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     66616    
unix  3      [ ]         STREAM     CONNECTED     63959    @/tmp/.X11-unix/X10
unix  3      [ ]         STREAM     CONNECTED     59388    
unix  3      [ ]         STREAM     CONNECTED     213161   
unix  3      [ ]         STREAM     CONNECTED     62254    @/tmp/.X11-unix/X10
unix  3      [ ]         STREAM     CONNECTED     66332    
unix  3      [ ]         STREAM     CONNECTED     58286    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     68837    
unix  3      [ ]         STREAM     CONNECTED     53840    
unix  3      [ ]         STREAM     CONNECTED     37214    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     59060    
unix  3      [ ]         STREAM     CONNECTED     69036    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     67741    /run/user/1001/at-spi/bus_10.0
unix  3      [ ]         STREAM     CONNECTED     69860    
unix  3      [ ]         STREAM     CONNECTED     53600    
unix  3      [ ]         STREAM     CONNECTED     52704    
unix  3      [ ]         STREAM     CONNECTED     69855    
unix  3      [ ]         DGRAM      CONNECTED     20088    
unix  3      [ ]         STREAM     CONNECTED     60517    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     213165   @/tmp/.ICE-unix/664
unix  3      [ ]         STREAM     CONNECTED     67256    
unix  3      [ ]         STREAM     CONNECTED     56909    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     68841    
unix  3      [ ]         STREAM     CONNECTED     67736    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     67181    
unix  3      [ ]         STREAM     CONNECTED     67101    @/tmp/.X11-unix/X10
unix  3      [ ]         STREAM     CONNECTED     20073    
unix  3      [ ]         STREAM     CONNECTED     69884    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     69865    
unix  3      [ ]         STREAM     CONNECTED     66091    /run/user/1001/bus
unix  3      [ ]         STREAM     CONNECTED     67723    @/tmp/.X11-unix/X10
unix  3      [ ]         STREAM     CONNECTED     58285    
unix  3      [ ]         STREAM     CONNECTED     31424    @8754299d578c001/bus/systemd-network/bus-api-network
unix  3      [ ]         STREAM     CONNECTED     32270    @d5440b04cdeecaac/bus/systemd-logind/system
unix  3      [ ]         STREAM     CONNECTED     52785    @18fb2875985118a4/bus/systemd/bus-system
unix  3      [ ]         STREAM     CONNECTED     32137    @87b69359aaa1a98/bus/systemd-resolve/bus-api-resolve
unix  3      [ ]         STREAM     CONNECTED     54990    @bafb120510c861df/bus/systemd/bus-api-user
unix  3      [ ]         STREAM     CONNECTED     35982    @c0ac970733b9afb4/bus/systemd/bus-api-system

```


## Running processes


```
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.2  0.3  22448 13524 ?        Ss   Sep27   0:07 /sbin/init
root          53  0.0  0.4  66880 17668 ?        Ss   Sep27   0:03 /usr/lib/syst
root         113  0.0  0.1  26036  7712 ?        Ss   Sep27   0:00 /usr/lib/syst
systemd+     245  0.0  0.3  21464 12884 ?        Ss   Sep27   0:00 /usr/lib/syst
systemd+     264  0.0  0.2  18996  9416 ?        Ss   Sep27   0:00 /usr/lib/syst
root         291  0.0  0.1 311124  7900 ?        Ssl  Sep27   0:00 /usr/libexec/
avahi        292  0.0  0.1   8696  4496 ?        Ss   Sep27   0:00 avahi-daemon:
message+     293  0.1  0.1  10268  5808 ?        Ss   Sep27   0:03 @dbus-daemon 
polkitd      298  0.0  0.2 384368 10900 ?        Ssl  Sep27   0:01 /usr/lib/polk
root         309  0.0  0.2  18020  8848 ?        Ss   Sep27   0:00 /usr/lib/syst
root         311  0.0  0.3 468600 13288 ?        Ssl  Sep27   0:00 /usr/libexec/
avahi        313  0.0  0.0   8424  1524 ?        S    Sep27   0:00 avahi-daemon:
root         436  0.0  0.2  18152 11492 ?        Ss   Sep27   0:00 /usr/sbin/wpa
root         465  0.0  0.0   7224  2696 ?        Ss   Sep27   0:00 /usr/sbin/cro
root         483  0.0  0.4 334248 18984 ?        Ssl  Sep27   0:02 /usr/sbin/Net
root         484  0.0  0.0   6148  2104 pts/0    Ss+  Sep27   0:00 /sbin/agetty 
root         488  0.0  0.1  16340  4792 ?        S    Sep27   0:00 /usr/sbin/xrd
syslog       494  0.0  0.1 152872  5384 ?        Ssl  Sep27   0:00 /usr/sbin/rsy
xrdp         511  0.0  0.0  13120  2380 ?        S    Sep27   0:00 /usr/sbin/xrd
root         648  0.0  0.1  16184  4536 ?        S    Sep27   0:00 /usr/sbin/xrd
contrac+     652  0.0  0.2  20356 11492 ?        Ss   Sep27   0:00 /usr/lib/syst
contrac+     654  0.0  0.0  21200  3548 ?        S    Sep27   0:00 (sd-pam)
contrac+     663  0.0  0.3 507508 13740 ?        Ssl  Sep27   0:00 /usr/bin/puls
contrac+     664  0.0  1.9 564080 79292 ?        Sl   Sep27   0:01 xfce4-session
contrac+     665  0.1  2.6 353660 106480 ?       Sl   Sep27   0:06 /usr/lib/xorg
contrac+     672  0.0  0.1  89776  6164 ?        Sl   Sep27   0:00 /usr/sbin/xrd
rtkit        673  0.0  0.0  22940  3464 ?        SNsl Sep27   0:00 /usr/libexec/
contrac+     696  0.0  0.1   9996  5780 ?        Ss   Sep27   0:00 /usr/bin/dbus
contrac+     766  0.0  0.0   8304  1536 ?        Ss   Sep27   0:00 /usr/bin/ssh-
contrac+     783  0.0  0.1 383300  7988 ?        Ssl  Sep27   0:00 /usr/bin/ibus
contrac+     784  0.0  0.0   7740  3440 ?        S    Sep27   0:01 /bin/bash /us
contrac+     797  0.0  0.1 312072  7888 ?        Ssl  Sep27   0:00 /usr/libexec/
contrac+     810  0.0  0.1 234472  7076 ?        Sl   Sep27   0:00 /usr/libexec/
contrac+     811  0.0  2.2 641912 88256 ?        Sl   Sep27   0:00 /usr/libexec/
contrac+     812  0.3  2.1 570440 86652 ?        Sl   Sep27   0:11 /usr/libexec/
contrac+     814  0.0  1.9 489672 78600 ?        Sl   Sep27   0:01 /usr/libexec/
contrac+     819  0.0  0.1 308252  7168 ?        Sl   Sep27   0:00 /usr/libexec/
contrac+     825  0.0  0.2 382908  8404 ?        Ssl  Sep27   0:00 /usr/libexec/
contrac+     832  0.0  0.1   9560  5132 ?        S    Sep27   0:00 /usr/bin/dbus
contrac+     851  0.0  0.4 478020 16580 ?        Ssl  Sep27   0:00 /usr/libexec/
contrac+     853  0.0  0.2 236044  8136 ?        Sl   Sep27   0:00 /usr/libexec/
contrac+     867  0.0  0.1 534388  7336 ?        Ssl  Sep27   0:00 /usr/libexec/
contrac+     874  0.0  0.1 307136  6048 ?        Ssl  Sep27   0:00 /usr/libexec/
contrac+     879  0.0  0.0 155540  3184 ?        SLsl Sep27   0:00 /usr/bin/gpg-
root         891  0.0  0.0   2704  2048 ?        Ss   Sep27   0:00 fusermount3 -
contrac+     892  0.0  2.9 1265048 118908 ?      Sl   Sep27   0:02 xfwm4
contrac+     895  0.0  0.6 412408 24484 ?        Ssl  Sep27   0:00 /usr/libexec/
contrac+     915  0.0  0.1 234596  7232 ?        Sl   Sep27   0:00 /usr/libexec/
contrac+     943  0.0  0.6 302320 27484 ?        Sl   Sep27   0:00 xfsettingsd
root         947  0.0  0.2 314096  8632 ?        Ssl  Sep27   0:00 /usr/libexec/
contrac+     961  0.1  0.8 417672 35116 ?        Sl   Sep27   0:05 xfce4-panel
contrac+     966  0.0  0.6 412280 24116 ?        Sl   Sep27   0:00 Thunar --daem
contrac+     973  0.0  1.4 505388 59052 ?        Sl   Sep27   0:01 xfdesktop
contrac+     989  0.0  0.8 416504 32800 ?        Ssl  Sep27   0:00 /usr/lib/x86_
contrac+     993  0.0  0.9 646300 36376 ?        Sl   Sep27   0:00 nm-applet
contrac+     997  0.0  0.4 257908 16648 ?        Sl   Sep27   0:00 /usr/lib/poli
contrac+    1005  0.0  0.7 415048 31944 ?        Sl   Sep27   0:00 /usr/lib/x86_
contrac+    1006  0.0  1.0 651504 41324 ?        Sl   Sep27   0:00 /usr/lib/x86_
contrac+    1007  0.0  0.9 458320 38864 ?        Sl   Sep27   0:00 /usr/lib/x86_
contrac+    1025  0.0  0.2 460584  9896 ?        Ssl  Sep27   0:00 /usr/libexec/
contrac+    1042  0.0  0.1 308536  6852 ?        Ssl  Sep27   0:00 /usr/libexec/
contrac+    1061  0.0  0.1 307600  6420 ?        Ssl  Sep27   0:00 /usr/libexec/
contrac+    1063  0.0  0.7 340068 28704 ?        Sl   Sep27   0:00 /usr/lib/x86_
contrac+    1080  0.0  0.1 307568  6480 ?        Ssl  Sep27   0:00 /usr/libexec/
contrac+    1086  0.0  0.1 387208  7936 ?        Ssl  Sep27   0:00 /usr/libexec/
contrac+    1103  0.0  0.2 533536  8824 ?        Sl   Sep27   0:00 /usr/libexec/
contrac+    1113  0.0  0.1 234096  6444 ?        Ssl  Sep27   0:00 /usr/libexec/
xrdp        8053  1.1  0.5  30080 23020 ?        R    00:40   0:06 /usr/sbin/xrd
contrac+    8083  0.0  0.1 307500  6328 ?        Sl   00:40   0:00 /usr/lib/x86_
contrac+    8917  0.8  1.1 619060 48008 ?        Sl   00:46   0:02 xfce4-termina
contrac+    8929  0.0  0.1   9068  5300 pts/1    Ss   00:46   0:00 bash
root        8949  0.0  0.1  17348  7216 pts/1    S+   00:46   0:00 sudo su
root        8971  0.0  0.0  17348  2620 pts/2    Ss   00:46   0:00 sudo su
root        8972  0.0  0.1   9820  4328 pts/2    S    00:46   0:00 su
root        8973  0.0  0.1   8004  4244 pts/2    S    00:46   0:00 bash
contrac+    9607  0.0  0.0   6112  1920 ?        S    00:50   0:00 sleep 3
root        9608  0.0  0.1  11452  4428 pts/2    R+   00:50   0:00 ps aux

```




## discovery of the hostname

Running a commnad:
```bash
avahi-resolve-address 10.159.143.45
```
reveal a host

```

10.159.143.45	jumpbox.lxd

```