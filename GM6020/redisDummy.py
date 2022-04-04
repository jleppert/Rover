import redis
import msgpack

r = redis.Redis(
	host='127.0.0.1',
	port=6379)

print('Publishing motVals to redis')

valsArray = msgpack.packb([1500,0000,0000,0000])
r.set('motVals', valsArray)
# 		r.set('motVals', valsArray)

# while True:
# 	for i in range(30000):

# 		valsArray = msgpack.packb([i,i,-i,-i])
# 		r.set('motVals', valsArray)

# 	for i in range(30000,0,-1):
# 		valsArray = msgpack.packb([i,i,-i,-i])
# 		r.set('motVals', valsArray)
