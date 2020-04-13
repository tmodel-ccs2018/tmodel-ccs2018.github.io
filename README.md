Overview
--------

This is the landing page for the following research publication:

**Privacy-Preserving Dynamic Learning of Tor Network Traffic**  
_Proceedings of the 25th ACM Conference on Computer and Communication Security (CCS 2018)_  
by [Rob Jansen](https://www.robgjansen.com), [Matthew Traudt](https://matt.traudt.xyz), and [Nicholas Hopper](https://www-users.cs.umn.edu/~hoppernj)
\[[Full paper available here](https://www.robgjansen.com/publications/tmodel-ccs2018.pdf)\]

If you reference this paper or use any of the data or models provided on this page, please cite the paper. Here is a bibtex entry for latex users:

```
@inproceedings{tmodel-ccs2018,
author = {Rob Jansen and Matthew Traudt and Nicholas Hopper},
title = {Privacy-Preserving Dynamic Learning of {Tor} Network Traffic},
booktitle = {25th ACM Conference on Computer and Communications Security (CCS)},
year = {2018},
note = {See also \url{https://tmodel-ccs2018.github.io}},
}
```

The research included privacy-preserving measurement and Tor network simulation components.

Measurement
-----------

Measurement of Tor was done using PrivCount, a tool for privacy-preserving Tor statistics aggregation, along with a modified version of Tor. We modified each of these tools for the purposes of dynamically learning and modeling Tor traffic:

##### PrivCount Code

Traffic learning and modeling changes have been merged upstream!

  + git repo: `git@github.com:privcount/privcount.git`
  + at branch `master`  
    (since commit `c707af2a3f3e4ae7aa16b672f4d83ae1806f597d`)
  + git web: [https://github.com/privcount/privcount](https://github.com/privcount/privcount)

The version we used for our experiments:

  + git repo: `git@github.com:robgjansen/privcount.git`
  + using branch `research/tmodel/train-v3`
  + git web: [https://github.com/robgjansen/privcount/tree/research/tmodel/train-v3](https://github.com/robgjansen/privcount/tree/research/tmodel/train-v3)

##### Tor Code

Traffic learning and modeling changes have been merged upstream!

  + git repo: `git@github.com:privcount/tor.git`
  + at branch `privcount-master`  
    (since commit `38d6e2dafbc0669b38d2564426b21e67d83fea3f`)
  + git web: [https://github.com/privcount/tor](https://github.com/privcount/tor)

The version we used for our experiments:

  + git repo: `git@github.com:robgjansen/tor.git`
  + using branch `research/tmodel/train-v3-03210`
  + git web: [https://github.com/robgjansen/tor/tree/research/tmodel/train-v3-03210](https://github.com/robgjansen/tor/tree/research/tmodel/train-v3-03210)

##### Data

See [data/privcount](https://github.com/tmodel-ccs2018/tmodel-ccs2018.github.io/tree/master/data/privcount) in the repo. Each measurement number corresponds to the measurement number listed in Table 2 in [the paper](https://www.robgjansen.com/publications/tmodel-ccs2018.pdf). Measurements 1-7 are ground truth measurements, measurement 8 includes 14 iterations for learning the packet model, and measurement 9 includes 14 iterations for learning the stream model.

The best packet model was from [measurement 8-9](data/privcount/measurement8/9/privcount.traffic.model.1522196794-1522283493.json), and the best stream model was from [measurement 9-9](data/privcount/measurement9/9/privcount.traffic.model.1524154791-1524241191.json).

<!--
| Measurement| Data files |
|------------|-------------|
| Entry 1    | [PrivCount tallies](data/privcount/measurement1/privcount.tallies.1508707017-1508793717.json), [relay weights](data/privcount/measurement1/weights.txt) |
| Entry 2    | [PrivCount tallies](), [relay weights]() |
| Exit 3     | [PrivCount tallies](), [relay weights]() |
| Exit 4     | [PrivCount tallies](), [relay weights]() |
| Exit 5     | [PrivCount tallies](), [relay weights]() |
| Exit 6     | [PrivCount tallies](), [relay weights]() |
| Exit 7     | [PrivCount tallies](), [relay weights]() |
| Exit 8-1   | [PrivCount tallies](), [relay weights](), [traffic model]() |
| Exit 9-1   | [PrivCount tallies](), [relay weights](), [traffic model]() |
-->

Simulation
----------

Simulation was done using Shadow, a full network simulation tool that directly executes Tor.

##### Shadow Code

Changes have been merged upstream!

  + git repo: `git@github.com:shadow/shadow.git`
  + at branch: `master`  
    (our experiments were run at commit: `322d8e047ae9adbc7ddbdfdae0c6aec073eb2374`)
  + git web: [https://github.com/shadow/shadow](https://github.com/shadow/shadow)

You can run Shadow with your own version of Tor to help with your own research.

If you want to export PrivCount events in order to count the number of streams, circuits, bytes, etc. as we did in the paper, you'll need to use the Tor `research/tmodel/train-v3-03210` branch listed above. Additionally, due to [a bug in PrivCount](https://github.com/privcount/privcount/issues/510), you should also apply our workaround patch to TGen to make sure all stream events get recorded correctly:
[data/shadow/workaround_for_privcount_stream_bug.patch](data/shadow/workaround_for_privcount_stream_bug.patch)

##### Shadow Network Configuration

Section 6.1.1 in [the paper](https://www.robgjansen.com/publications/tmodel-ccs2018.pdf) describes our approach to creating an Internet model for using as Shadow's network configuration. That methodology yielded a network graph graphml file that we used in our Shadow simulations. We also back-ported the network graph for a previous stable version of Shadow. These files should be decompressed and copied to `~/.shadow/share`.

  + [Network graph file for use with Shadow v1.13.0](data/shadow/network/atlas.201801.shadow113.graphml.xml.xz) (the version we used in our experiments)
  + [Network graph file for use with Shadow v1.12.1](data/shadow/network/atlas.201801.shadow112.graphml.xml.xz) (older stable version of Shadow)

Later research has used a version of our Internet model that does not contain packet loss on the links between the core routers in the topology. We host this version of our model for posterity.

  + [Network graph file for use with Shadow v1.13.0](data/shadow/network/atlas-lossless.201801.shadow113.graphml.xml.xz) (lossless links between core routers)

We've compiled the scripts necessary to gather the input data and compile it
into a topology file [here](https://github.com/shadow/atlas). See
[here](atlas-data.md) for links to the input data we used.

##### Shadow Host Configuration

Our Shadow experiments used the client behavior models that we discuss in the paper. You can incorporate these models into your own Shadow experiments.

  + Protocol TGen models for [BitTorrent clients](data/shadow/tgen/tgen.protocol.bittorrent.model.graphml.xml.xz) and [HTTP clients](data/shadow/tgen/tgen.protocol.http.model.graphml.xml.xz)
  + PrivCount TGen HMM models for [stream](data/shadow/tgen/tgen.privcount.stream.model.graphml.xml.xz) and [packet](data/shadow/tgen/tgen.privcount.packet.model.graphml.xml.xz) generation

If you want to repeat our experiments, Section 6.1.2 in [the paper](https://www.robgjansen.com/publications/tmodel-ccs2018.pdf) describes our host configuration for each of the 3 TGen models we tested. Here are the Shadow configurations needed to run each experiment. Run time is estimated and assumes a 32-core server with 30 Shadow worker threads.

| Client Model | # Relays | # Clients | RAM       | Run time |
|--------------|----------|-----------|-----------|----------|
| [Single file](data/shadow/hosts/shadowtor-2000r-60000c-singlefile-config.tar.xz)  | 2,000    | 60,000    | ~1.25 TiB | ~1 week  |
| [Protocol](data/shadow/hosts/shadowtor-2000r-13730c-archive-config.tar.xz)     | 2,000    | 13,730    | ~300 GiB  | ~1 week  |
| [PrivCount](data/shadow/hosts/shadowtor-2000r-129419c-privcount-config.tar.xz)    | 2,000    | 129,419   | ~2.75 TiB | ~1 month |
