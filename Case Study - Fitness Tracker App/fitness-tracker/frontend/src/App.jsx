import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Signup from "./components/Signup";
import Login from "./components/Login";
import Dashboard from "./components/Dashboard";
import Workouts from "./components/Workouts";
import Analytics from "./components/Analytics";
import Profile from "./components/Profile";
import Home from "./components/Home";
import Navbar from "./components/Navbar";   
import Footer from "./components/Footer"; 

export default function App() {
  return (
    <Router>
      <div style={{ backgroundColor: "black", minHeight: "100vh", color: "white" }}>
        {/* Navbar */}
        <Navbar />

        {/* Routes */}
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/login" element={<Login />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/analytics" element={<Analytics />} />
          <Route path="/profile" element={<Profile />} />
        </Routes>

        <Footer />
      </div>
    </Router>
  );
}
