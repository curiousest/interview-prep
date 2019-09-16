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

### Consistent hashing

* S: # shards
* H: numeric hash

If we assign the key to shard H % S, we have to move data whenever we add a shard (because H % S of every key will change).

## High availability in system design

asdf

## High consistency in system design

asdf