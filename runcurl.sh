set -eux

for i in {1..10}; do
    curl -X GET http://localhost:3000/
    curl -X GET http://localhost:3000/error
done
