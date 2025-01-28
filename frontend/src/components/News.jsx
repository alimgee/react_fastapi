// src/components/News.jsx

import React, { useEffect, useState } from 'react';
import axios from 'axios';

const News = () => {
  const [news, setNews] = useState([]);

  useEffect(() => {
    const fetchNews = async () => {
      try {
        const response = await axios.get('http://localhost:8000/news/');
        setNews(response.data);
      } catch (error) {
        console.error('Error fetching news:', error);
      }
    };
    fetchNews();
  }, []);

  return (
    <div>
      <h1>News Feed</h1>
      <ul>
        {news.map((item) => (
          <li key={item.id}>
            <h2>{item.title}</h2>
            <p>{item.content}</p>
            <a href={item.link} target="_blank" rel="noopener noreferrer">Read more</a>
            <p>{item.date}</p>
            <p>{item.provider}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default News;
