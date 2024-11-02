import React, { useState } from 'react';
import axios from 'axios';

function BookingPage() {
    const [formData, setFormData] = useState({ name: '', email: '', booking_time: '' });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        await axios.post('/book', formData);
        alert('Booking successful!');
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" name="name" placeholder="Name" onChange={handleChange} />
            <input type="email" name="email" placeholder="Email" onChange={handleChange} />
            <input type="datetime-local" name="booking_time" onChange={handleChange} />
            <button type="submit">Book</button>
        </form>
    );
}

export default BookingPage;
