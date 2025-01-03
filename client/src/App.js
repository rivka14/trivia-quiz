import "./App.css";
import React from "react";
import { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from "./pages/HomePage/HomePage";
import Login from "./pages/LoginForm/LoginForm";
import Register from "./pages/RegisterForm/RegisterForm";
import CreateQuiz from "./pages/CreateQuiz/CreateQuiz";
import QuizPage from "./pages/QuizPage/QuizPage";
import Quizzes from "./pages/Quizzes/Quizzes";
import Layout from "./components/Layout/Layout"
import NavBar from "./components/Navbar/NavBar";
const App = () => {
  const [userName, setUserName] = useState(null);

  return (
    <>
      <Router>
        <NavBar />
        <Layout>
          <Routes>
            <Route path="/" element={<Home userName={userName} setUserName={setUserName} />} />
            <Route path="/login" element={<Login setUserName={setUserName} />} />
            <Route path="/register" element={<Register />} />
            <Route path="/create-quiz" element={<CreateQuiz />} />
            <Route path="/quiz" element={<QuizPage userName={userName} />} />
            <Route path="/quizzes" element={<Quizzes />} />
          </Routes>
        </Layout>
      </Router>
    </>
  );
}

export default App;