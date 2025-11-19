# dokklas

Document classification program. (Vapor so far)

## (intended) Usage

The program is an (offline) script that scans a directory 
recursively for all documents under it. It 

1. first erects a corpus, that is a statistic of all the
   words that occurs in all documents found,
2. it erects a statistic for each document, and uses the
   corpus to determine the *most specialized words* for that
   document in relation to the corpus, and selects the most
   specialized words as keywords for that document.
   
You must have read access to all the documents in the
directory that is classified.

### Initialization

Initially classify or reclassify a directory:

```
$ dokklas --classify
```

This command scans the directory for all documents
and classify them.

### Finding documents

Find document classified with key 'network':

```
$ dokklas 'network'
network_intro_1.docx     network fundamentals history
network_intro_2.docx     network fundamentals addresses introduction
network_ipv4_1.docx      network fundamentals addresses IPv4
network_ipv4_LAN.docx    network fundamentals addresses IPv4 LAN private
network_ipv4_DHCP.docx   network fundamentals addresses IPv4 LAN private dynamicip
network_ipv6_1.docx      network fundamentals addresses IPv6
network_ipv6_LAN.docx    network fundamentals addresses IPv6 LAN private
$
```

Find a document classified with key 'network' and 'IPv6':

```
$ dokklas 'network, IPv6'
network_ipv6_1.docx      network fundamentals addresses IPv6
network_ipv6_LAN.docx    network fundamentals addresses IPv6 LAN private
$
```

Find a document classified with key 'private' and 'IPv4' or 'IPv6':

```
$ dokklas 'private, (IPv4; IPv6)'
network_ipv4_LAN.docx    network fundamentals addresses IPv4 LAN private
network_ipv4_DHCP.docx   network fundamentals addresses IPv4 LAN private dynamicip
network_ipv6_LAN.docx    network fundamentals addresses IPv6 LAN private
$ 
```

### Assessing a document

You assess a document when you want to classify it manually:

```
$ dokklas --assess N01_Network_topologies.pptx
network topology
$
```

You can reclassify a document by adding tags:

```
$ dokklas --amend 'LAN, WAN' N01_Network_topologies.pptx
$ dokklas --assess N01_Network_topologies.pptx
LAN WAN network topology
$ 
```

or by removing tags using the minus convention:

```
$ dokklas --amend '!LAN, !WAN' N01_Network_topologies.pptx
$ dokklas --assess N01_Network_topologies.pptx
network topology
$ 
```

### Reset a classification

Reset a directory classification:

```
$ dokklas --reset
```

Only if the classification is messed up beyond repair!
The classification is removed and the entire directory 
is rescanned and classified.