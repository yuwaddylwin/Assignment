import express from 'express';
import axios from 'axios';

// create express app object
const app = express();
const port = 3000;

// Configure EJS view engine and static files
app.set('view engine', 'ejs');
app.use(express.static('public'));

// Reusable function to fetch a random cocktail
async function getRandomCocktail() {
    const response = await axios.get('https://www.thecocktaildb.com/api/json/v1/1/random.php');
    return response.data;
}

// Reusable function to fetch cocktails by name
async function getCocktailByName(name) {
    const response = await axios.get(`https://www.thecocktaildb.com/api/json/v1/1/search.php?s=${name}`);
    return response.data;
}

// Routes
// -----------------------------------------
// Home route
app.get('/', async (req, res) => {
    const data = await getRandomCocktail();
    const cocktail = data.drinks[0];
    res.render('index', { cocktail });
});

// Route to fetch cocktails by name
app.get('/cocktails/name/:cocktailname', async (req, res) => {
    const name = req.params.cocktailname;
    const data = await getCocktailByName(name);
    res.json(data);
});

// Route to get random cocktail (JSON response)
app.get('/cocktails/random', async (req, res) => {
    const data = await getRandomCocktail();
    res.json(data);
});

// Server setup
app.listen(port, () => {
    console.log(`Cocktail app is running on http://localhost:${port}`);
});
