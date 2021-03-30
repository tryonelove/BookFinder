## Books Recommendation System
___
### Content - Based filtering

A content-based recommender works with data that the user provides, either _explicitly_ (rating, adding to wishlist) or _implicitly_ (clicking on a link). Based on that data, a user profile is generated, which is then used to make suggestions to the user. As the user provides more inputs or takes actions on those recommendations, the engine becomes more and more accurate.
A recommender system has to decide between two methods for information delivery when providing the user with recommendations:
- Exploitation. The system chooses books similar to those for which the user has already expressed a preference.
- Exploration. The system chooses books where the user profile does not provide evidence to predict the user’s reaction.
To personalise our recommendations, I am going to build an engine that computes similarity between books based on certain metrics and suggests books that are most similar to a particular book that a user read/added to wishlist. Since we will be using book's metadata to build this engine.
  
#### ![equation](http://www.sciweavers.org/tex2img.php?eq=TF%20%5Ctimes%20IDF&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)
  
The ![equation](http://www.sciweavers.org/tex2img.php?eq=TF%20%5Ctimes%20IDF&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)
 algorithm is used to weigh a keyword in any document and assign the importance to that keyword based on the number of times it appears in the document. Put simply, the higher the TF$\times$IDF score (weight), the rarer and more important the term, and vice versa.  
  
The TF (term frequency) of a word is the number of times it appears in a books's genre. When you know it, you’re able to see if you’re using a term too often or too infrequently.
```python
TF(t) = (Number of times term t appears in a document) / (Total number of terms in the document)
```

The IDF (inverse document frequency) of a word is the measure of how significant that genre is in the whole corpus.

```python
IDF(t) = log_e(Total number of documents / Number of documents with term t in it)
```

#### Cosine Similarity

I will be using the Cosine Similarity to calculate a numeric quantity that denotes the similarity between two movies. Mathematically, it is defined as follows:

$cosine(x,y)=\frac{x.y^T}{||x||.||y||}$
  
Since we have used the TF-IDF Vectorizer, calculating the Dot Product will directly give us the Cosine Similarity Score. Therefore, we will use sklearn's linear_kernel instead of cosine_similarities since it is much faster.

### Usage

Firstly, you need to run in console ```refresh_recommendations.py``` file to populate ```users_recommendations``` table.

```python
python refresh_recommendations -hst <localhost> -u <username> -p <password> -db  <database_name> 
```

Create a new RecommendationEngine object.

```python
rec_engine = RecommendationEngine()
```

To get recommendations you need to run the following steps:

```python
rec_enginde.connect_to_db('db_name', 'username', 'password', 'localhost')
book_titles_ids = rec_engine.get_recommendations(1)
rec_engine.close_db_connection()
```

