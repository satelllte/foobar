const blossom = require('edmonds-blossom')

const data = [
  [0, 1, true],
  [0, 2, true],
  [1, 2, true],
]

const result = blossom(data)

console.info('result: ', result)
