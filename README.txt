:::::  Self Contained CloudStack, using Vagrant and Simulator ::::: 

Description: Readily available Cloudstack with data center. With the help of Vagrant boxes and simulator, a thin ubuntu vm is provisioned, required software and Cloudstack are installed, followed by a deploy data center automatically.

Advantages:
1. Simple, on the fly, easy for Cloudstack demos, useful for new users, for developers to validate their changes, locally using simulator. 

2.  Need not worry anything about downloading, installing Cloudstack, or its dependent softwares and installations etc, we can now have Cloudstack up and running with few simple commands. 

3. As well, it will now provide a ready made data center available inside Cloudstack, thus need not worry about understanding of creating zones,pods, ..hosts,... storage, etc.

Usage:

1. Install Vagrant ( EX: apt-get install vagrant, preferably its latest version http://www.vagrantup.com/downloads.html )

2. Retrieve the code from below link
https://github.com/bvbharatk/VagrantSimulator
 
3. By default, it will create Cloudstack for 4.4-forward branch, but we can change it to whichever branch we want. Once vagrant simulator code is downloaded,  we need to edit the below parameters for required branch under "bootstrap.sh" and then proceed further.

branch='4.4-forward'

4. Under "VagrantSimulator" dir, run commands, “vagrant init", "vagrant up”

Now, we can login to CS  and see Cloudstack with ready made data center available.

Note:

1 . Once we run vagrant up command, it will download good amount of content including a ubuntu box, cs and its dependencies etc. This may take some time. Idea is to parallelize this procedure in next cut. 

Hope it is useful!!






:::::  Self Contained CloudStack, using Vagrant and Simulator ::::: 

