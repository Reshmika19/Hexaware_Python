import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import Footer from "../components/Footer";
import ft2 from "../images/ft2.jpg";

export default function Login() {
  const [formData, setFormData] = useState({ email: "", password: "" });
  const [message, setMessage] = useState("");
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage("");

    try {
      const res = await fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      const data = await res.json();
      if (res.ok) {
        setMessage("Login successful!");
        localStorage.setItem("token", data.access_token);
        localStorage.setItem("user", JSON.stringify(data.user));
        navigate("/dashboard");
      } else {
        setMessage( data.msg);
      }
    } catch (error) {
      setMessage(" Error connecting to server.");
    }
  };

  return (
    <div className="d-flex flex-column min-vh-100" style={{ backgroundColor: "black", color: "white" }}>
      
      {/* Centered Container */}
      <div className="container flex-grow-1 d-flex justify-content-center align-items-center py-5">
        <div 
          className="d-flex rounded overflow-hidden w-100" 
          style={{ 
            backgroundColor: "#111", 
            maxWidth: "900px", 
            minHeight: "500px",
            boxShadow: "0 0 20px 5px rgba(153, 41, 234, 0.5)" 
          }}
        >
          {/* Left Side - Image */}
          <div className="w-50 d-none d-md-block">
            <img 
              src={ft2} 
              alt="Fitness" 
              className="h-100 w-100"
              style={{ objectFit: "cover", borderTopLeftRadius: "10px", borderBottomLeftRadius: "10px" }}
            />
          </div>

          {/* Right Side - Form */}
          <div className="w-100 w-md-50 p-5 d-flex flex-column justify-content-center">
            <h3 className="text-center mb-4" style={{ color: "#9929EA", fontFamily: "'Poppins', sans-serif", fontWeight: "700", fontSize: "1.8rem" }}>
              Login
            </h3>

            {message && (
              <div 
                className="text-center py-2 rounded mb-3" 
                style={{ 
                  backgroundColor: message.includes("✅") ? "#9929EA" : "#FF4C4C", 
                  color: "#fff" 
                }}
              >
                {message.replace("✅ ", "").replace("❌ ", "")}
              </div>
            )}

            <form onSubmit={handleSubmit}>
              <div className="mb-3">
                <label className="form-label">Email</label>
                <input type="email" className="form-control" name="email" value={formData.email} onChange={handleChange} required />
              </div>
              <div className="mb-3">
                <label className="form-label">Password</label>
                <input type="password" className="form-control" name="password" value={formData.password} onChange={handleChange} required />
              </div>

              <button 
                type="submit" 
                className="btn w-100 mt-3 shadow-sm"
                style={{ 
                  backgroundColor: "#9929EA", 
                  color: "#fff", 
                  borderRadius: "25px", 
                  fontWeight: "600", 
                  fontSize: "1rem",
                  transition: "0.3s"
                }}
                onMouseEnter={(e) => (e.target.style.backgroundColor = "#7a1dbd")}
                onMouseLeave={(e) => (e.target.style.backgroundColor = "#9929EA")}
              >
                Login
              </button>
            </form>

            <p className="mt-3 text-center" style={{ color: "#ccc" }}>
              Don't have an account? <Link to="/signup" style={{ color: "#9929EA" }}>Signup</Link>
            </p>
          </div>
        </div>
      </div>

    </div>
  );
}

