
## **Theoretical Question: Data Structures & Functional Programming**

### Task:

- **Characteristics and Use Cases**: Describe the characteristics of Python's data structures (list, tuple, set, dictionary) and provide a scenario for each.
- **Functional Programming Integration**: Explain how lambda expressions can be used with two of these structures, and provide examples.

### Answer:

- **List**: Mutable, ordered, indexed, allows duplicates.  
  **Use case**: Storing mutable data (e.g., age records).
  
- **Tuple**: Immutable, ordered, indexed, allows duplicates.  
  **Use case**: Securely storing immutable data (e.g., dictionary keys).
  
- **Set**: Mutable, unordered, unindexed, no duplicates.  
  **Use case**: Storing unique items (e.g., unique IDs).
  
- **Dictionary**: Keys are immutable, values are mutable, ordered (Python 3.7+), no duplicate keys.  
  **Use case**: Mapping keys to values (e.g., product IDs to prices).

- **Lambda with Lists**: Useful for sorting or filtering data.
- **Lambda with Tuples**: Useful for filtering conditions.

---

## **Question 1: Basic Data Retrieval**

### Dataset:

```python
feedback_data = {
    'positive': {
        'Mohamed': {'Great service and friendly staff.', 'Loved the coffee!'},
        'Fatima': {'Loved the ambience and the music.'},
        'Youssef': {'Helpful staff and quick service.'}
    },
    'neutral': {
        'Amira': {'Long wait time, but good food.'},
        'Khalid': {'Could improve the cleanliness.'}
    },
    'negative': {
        'Hussein': {'Unsatisfactory customer service.', 'Order was delayed.'}
    }
}
```

### Task:

Write a function `count_feedback()` to calculate the total number of feedback comments.

### Answer:

```python
def count_feedback():
    total = 0
    for sentiment in feedback_data:
        for person in feedback_data[sentiment]:
            total += len(feedback_data[sentiment][person])
    return total

print(count_feedback())
```

---

## **Question 2: Sentiment Analysis Count**

### Dataset:

```python
feedback_data = {
    'positive': {
        'Mohamed': {'Great service and friendly staff.', 'Loved the coffee!'},
        'Fatima': {'Loved the ambience and the music.'},
        'Youssef': {'Helpful staff and quick service.'}
    },
    'neutral': {
        'Amira': {'Long wait time, but good food.'},
        'Khalid': {'Could improve the cleanliness.'}
    },
    'negative': {
        'Hussein': {'Unsatisfactory customer service.', 'Order was delayed.'}
    }
}
```

### Task:

Write a function `count_by_sentiment()` to return the number of comments for each sentiment category.

### Answer:

```python
def count_by_sentiment():
    out = {}
    for sentiment in feedback_data:
        total = 0
        for person in feedback_data[sentiment]:
            total += len(feedback_data[sentiment][person])
        out[sentiment] = total
    return out

print(count_by_sentiment())
```

---

## **Question 3: Average Feedback Score**

### Dataset:

```python
feedback_data = {
    'positive': {
        'Mohamed': [('Great service and friendly staff.', 5), ('Loved the coffee!', 4)],
        'Fatima': [('Loved the ambience and the music.', 5)],
        'Youssef': [('Helpful staff and quick service.', 4)]
    },
    'neutral': {
        'Amira': [('Long wait time, but good food.', 3)],
        'Khalid': [('Could improve the cleanliness.', 2)]
    },
    'negative': {
        'Hussein': [('Unsatisfactory customer service.', 1), ('Order was delayed.', 1)]
    }
}
```

### Task:

Write a function `average_feedback_score()` to calculate the average score of all feedback.

### Answer:

```python
def average_feedback_score():
    total = 0
    comments = 0
    for sentiment in feedback_data:
        for person in feedback_data[sentiment]:
            for comment in feedback_data[sentiment][person]:
                comments += 1
                total += comment[1]
    return total / comments

print(average_feedback_score())
```

---

## **Question 4: Filtering Top Performers**

### Dataset:

```python
performance_data = [
    ("Ahmed", "Exceeds expectations in all tasks.", 5),
    ("Sara", "Meets all deadlines with high-quality work.", 4),
    ("John", "Needs improvement in teamwork.", 2),
    ("Lina", "Consistently goes above and beyond.", 5),
    ("Mark", "Shows creativity in problem-solving but can be late.", 3),
    ("Zara", "Excellent collaborator and communicator.", 4),
    ("Khalid", "Work is adequate but lacks initiative.", 2),
    ("Noor", "Outstanding leadership in project management.", 5)
]
```

### Task:

Write a function `top_performers()` to identify employees with a score of 4 or higher.

### Answer:

```python
def top_performers():
    top = list(filter(lambda x: x[2] >= 4, performance_data))
    out = list(map(lambda x: (x[0], x[1]), top))
    return out

print(top_performers())
```
