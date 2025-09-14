import React from "react";
import { Link, useNavigate } from "react-router-dom";
import { FaDumbbell } from "react-icons/fa";

const Navbar = () => {
  const navigate = useNavigate();
  const token = localStorage.getItem("token");

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    navigate("/login");
  };

  return (
    <nav
      className="navbar navbar-expand-lg"
      style={{
        backgroundColor: "#000",
        padding: "12px 30px",
        boxShadow: "0 2px 10px rgba(153,41,234,0.3)",
      }}
    >
      <div className="container-fluid d-flex justify-content-between align-items-center">
        {/* Brand */}
        <Link className="navbar-brand d-flex align-items-center" to="/">
          <FaDumbbell size={32} color="#9929EA" className="me-3" />
          <span
            style={{
              color: "#9929EA",
              fontFamily: "'Poppins', sans-serif",
              fontWeight: "700",
              fontSize: "1.7rem",
              letterSpacing: "1px",
            }}
          >
            Fitness Tracker
          </span>
        </Link>

        {/* Nav Links */}
        <ul className="navbar-nav d-flex flex-row align-items-center" style={{ gap: "20px" }}>
          {!token ? (
            <>
              <li className="nav-item">
                <Link
                  className="nav-link"
                  to="/login"
                  style={{
                    color: "#fff",
                    fontWeight: "600",
                    fontSize: "1.1rem",
                    padding: "6px 12px",
                    borderRadius: "6px",
                    transition: "0.3s",
                  }}
                  onMouseEnter={(e) => (e.target.style.backgroundColor = "#9929EA")}
                  onMouseLeave={(e) => (e.target.style.backgroundColor = "transparent")}
                >
                  Login
                </Link>
              </li>
              <li className="nav-item">
                <Link
                  className="nav-link"
                  to="/signup"
                  style={{
                    color: "#fff",
                    fontWeight: "600",
                    fontSize: "1.1rem",
                    padding: "6px 12px",
                    borderRadius: "6px",
                    transition: "0.3s",
                  }}
                  onMouseEnter={(e) => (e.target.style.backgroundColor = "#9929EA")}
                  onMouseLeave={(e) => (e.target.style.backgroundColor = "transparent")}
                >
                  Signup
                </Link>
              </li>
            </>
          ) : (
            <>
              <li className="nav-item">
                <Link
                  className="nav-link"
                  to="/profile"
                  style={{
                    color: "#fff",
                    fontWeight: "600",
                    fontSize: "1.1rem",
                    padding: "6px 12px",
                    borderRadius: "6px",
                    transition: "0.3s",
                  }}
                  onMouseEnter={(e) => (e.target.style.backgroundColor = "#9929EA")}
                  onMouseLeave={(e) => (e.target.style.backgroundColor = "transparent")}
                >
                  Profile
                </Link>
              </li>
              <li className="nav-item">
                <button
                  className="btn"
                  style={{
                    color: "#fff",
                    fontWeight: "600",
                    fontSize: "1.1rem",
                    backgroundColor: "transparent",
                    padding: "6px 12px",
                    borderRadius: "6px",
                    transition: "0.3s",
                  }}
                  onMouseEnter={(e) => (e.target.style.backgroundColor = "#9929EA")}
                  onMouseLeave={(e) => (e.target.style.backgroundColor = "transparent")}
                  onClick={handleLogout}
                >
                  Logout
                </button>
              </li>
            </>
          )}
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
