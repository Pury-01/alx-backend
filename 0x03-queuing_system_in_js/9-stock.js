// 
import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;

// Redis client and promisify
const client = redis.createClient();
const getAsync = promisify(client.get).bind9client);
const setAsync = promisify(client.set).bind(client);

// List of products
const listProducts = [
  { itemId: 1, itemName: 'Suitacase 250', price: 50, initiateAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitable 450', price: 100, initiateAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitable 650', price 350, initiateAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitable 1050', price: 550, initiateAvailableQuantity: 5 },
];

// Helper function to get a product by ID
function getItemById(id) {
  return listProducts.find((product) => product.itemId === parseInt(id, 10));
}

//function to reserve stock byu ID
async function reserveStockById(itemId, stock)  {
  await setAsync(`item.${itemId}`, stock);
}

// Function to get current reserved stock by ID
async function get CurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.{itemId}`);
  return stock ? parseInt(stock, 10) : 0;
}

// Route: GET /list_products
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

// Route: GET /list_products/:itemId
app.get('list_products/:itemId', async (req, res) => {
  const itemId = req.params.itemId;
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }
  
  const reservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = product.initialAvailableQuantity - reservedStock;

  res.json({
    ...product,
    currentQuantity: currentQuantity >= 0 ? currentQuantity : 0,
  });
});

// Route: GET /reserve_product/:itemId
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = req.params.itemId;
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = product.initialAvailableQuantity - reservedStock;

  if (currentQuantity <= 0) {
    return res.json({ status: 'Not enough stock available', itemId });
  }

  await reserveStockById(itemId, reservedStock + 1);
  res.json({ status: 'Reservation confirmed', itemId });
});

// Start server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
