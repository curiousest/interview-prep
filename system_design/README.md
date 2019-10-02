#

## Steps to Approach a Problem

1. Feature expectations: use cases and requirements
2. Estimations: estimate the scale. Will sharding be needed?
3. Design goals: consistency vs. availability, speed of reads/writes. 
4. High-level design: one-liner about each component and the interactions they have with one-another.
5. Deep dive on specifics.

## CAP Theorem in system design

You get 2/3 of: consistency, availability, and partition tolerance. In modern practice you need partition tolerance, so you're generally trading off consistency vs. availability.


## Caching in system design

Often use a hashmap to access data and linked list to track which items to evict from the cache.

### Access patterns

* Write through cache: write confirmed after sucessful write to both cache and db. Useful for quick re-reads. Higher write latency.
* Write around cache: write directly to db, cache reads from db on cache miss. Lower write load to cache and faster writes. Higher read latency on write followed by read.
* Write back cache: write directly to cache, then async sync with db. Faster writes. Risk losing the write if cache dies.


## Sharding in system design

* Data in a shard should fit into one machine completely
* Be wary of sharding vs. normalization becuase joins across machines is expensive

### Consistent hashing

* S: # shards
* H: numeric hash

If use `shard key = H % S` of the data to store, we have to move data whenever we add a shard (because `shard key = H % (S+1)` will cause every key to change).

Consistent hashing is where you pick some constant, C to calculate `shard key = H % C`, and shards are assigned to ranges of keys. This can be visualized as a ring where all shard key values lie somewhere on the ring and shards are assigned to ranges of keys.

Modified consistent hashing is where the shards are assigned to multiple non-contiguous ranges of keys so that when shards are added/removed, the reassignment of data is not concentrated on a few nodes and is instead spread out because all nodes have key ranges near a much larger number of nodes.

## High availability in system design

Have multiple (N) peer nodes instead of master/slave to handle writes.

Write request: one node accepts and forwards the write to W nodes, and waits for a quorum of acks before acking the write to the client.

Read request: one node accepts and confirms data with R nodes before responding to client.

For a read to be consistent, W + R > N. Adjust W and R depending on volume of reads/writes.

## High consistency in system design

Have a master that tracks which nodes each block of data has been successfully written to. All reads go through the master. Nodes that are out of date can ask the master where to retrieve blocks of data from. A standby master watches writes to the master and durably logs them elsewhere. If the active master goes down, the standby master can bring up a new active master from the logs.