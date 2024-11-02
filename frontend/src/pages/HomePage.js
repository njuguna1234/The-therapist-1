import React, { useState, useEffect } from 'react';
import axios from 'axios';

function HomePage() {
    const [content, setContent] = useState([]);

    useEffect(() => {
        axios.get('/content').then(response => {
            setContent(response.data);
        });
    }, []);

    return (
        <div>
            <h1>Content</h1>
            {content.map((item) => (
                <div key={item.id}>
                    <h2>{item.title}</h2>
                    <p>{item.body}</p>
                    {item.media_url && <img src={item.media_url} alt="Media" />}
                </div>
            ))}
        </div>
    );
}

export default HomePage;
