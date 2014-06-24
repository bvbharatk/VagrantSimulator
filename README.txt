:::::  Self Contained CloudStack, using Vagrant and Simulator ::::: 

Advantages:

1. Simple, on the fly, easy for cloudstack demos, useful for new users,  for developers to validate their changes, locally using simulator.

2. Need not worry anything about downloading,  installing Cloudstack, or its  dependent softwares and installations etc, we can now have CloudStack up and running with a single command. 

3. As well, it will now provide a ready made data center available inside CloudStack,  thus need not worry about understanding of creating zones,pods, ..hosts,... storages, etc.

Usage:
1. Install Vagrant ( EX: apt-get install vagrant, preferrably  its latest version http://www.vagrantup.com/downloads.html  )
2. Download the code from below link
https://github.com/bvbharatk/VagrantSimulator
3. cd to directory "CloudStackSimulator"
4. Run commands in sequence, “vagrant init","vagrant up”

Now, we can login to CS through ,  we can see with ready made data center available
