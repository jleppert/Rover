import redis
import msgpack

r = redis.Redis(
	host='127.0.0.1',
	port=6379)

print('Publishing motVals to redis')

while True:
	for i in range(30000):

		valsArray = msgpack.packb([i,i,-i,-i])
		r.set('motVals', valsArray)

	for i in range(30000,0,-1):
		valsArray = msgpack.packb([i,i,-i,-i])
		r.set('motVals', valsArray)
