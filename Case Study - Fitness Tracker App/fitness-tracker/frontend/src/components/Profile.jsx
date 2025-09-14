import React, { useState, useEffect } from "react";
import { FaUserCircle } from "react-icons/fa";
import { useNavigate } from "react-router-dom";

export default function Profile() {
  const [user, setUser] = useState(null);
  const [formData, setFormData] = useState({});
  const [showModal, setShowModal] = useState(false);
  const [message, setMessage] = useState("");
  const navigate = useNavigate();

  // Fetch profile data
  useEffect(() => {
    const token = localStorage.getItem("token");
    fetch("http://127.0.0.1:5000/user", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.msg) {
          setMessage("❌ " + data.msg);
        } else {
          setUser(data);
          setFormData(data);
        }
      })
      .catch((err) => console.error("Error fetching user:", err));
  }, []);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSave = async () => {
    try {
      const token = localStorage.getItem("token");
      const res = await fetch("http://127.0.0.1:5000/user", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(formData),
      });

      const data = await res.json();
      if (res.ok) {
        setUser(data.user);
        setMessage("✅ Profile updated successfully");
        setShowModal(false);
      } else {
        setMessage("❌ " + data.msg);
      }
    } catch (error) {
      setMessage("❌ Error connecting to server.");
    }
  };

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    navigate("/login");
  };

  if (!user)
    return <p style={{ color: "white", textAlign: "center" }}>Loading...</p>;

  return (
    <div style={{ backgroundColor: "black", minHeight: "100vh", padding: "20px" }}>
      {/* Back to Dashboard Button */}
      <br />
      <button
        className="btn mb-4"
        style={{
          backgroundColor: "#9929EA",
          color: "white",
          borderRadius: "8px", marginLeft: "20px",
        }}
        onClick={() => navigate("/dashboard")}
      >
        Back to Dashboard
      </button>

      <div
        style={{
          display: "flex",
          justifyContent: "center",
          paddingTop: "10px",
        }}
      >
        <div
          style={{
            display: "flex",
            background: "#111",
            borderRadius: "15px",
            padding: "30px",
            width: "800px",
            boxShadow: "0 0 15px rgba(153,41,234,0.4)",
          }}
        >
          {/* Left Panel */}
          <div
            style={{
              width: "250px",
              borderRight: "1px solid #333",
              paddingRight: "20px",
              textAlign: "center",
            }}
          >
            <FaUserCircle size={120} color="#9929EA" />
            <h4 className="mt-3" style={{ color: "white" }}>
              {user.name}
            </h4>
            <button
              className="btn w-100 mt-3"
              style={{
                backgroundColor: "#9929EA",
                color: "white",
                borderRadius: "8px",
              }}
              onClick={() => setShowModal(true)}
            >
              Edit Profile
            </button>
            <button
              className="btn w-100 mt-2"
              style={{
                backgroundColor: "white",
                color: "black",
                borderRadius: "8px",
              }}
              onClick={handleLogout}
            >
              Logout
            </button>
          </div>

          {/* Right Panel */}
          <div style={{ flex: 1, marginLeft: "30px" }}>
            <h2 style={{ color: "#9929EA", marginBottom: "20px" }}>
              Profile Details
            </h2>
            <div style={{ lineHeight: "2" }}>
              <p>
                <strong style={{ color: "#aaa" }}>Name:</strong> {user.name}
              </p>
              <p>
                <strong style={{ color: "#aaa" }}>Email:</strong> {user.email}
              </p>
              <p>
                <strong style={{ color: "#aaa" }}>Age:</strong> {user.age || "-"}
              </p>
              <p>
                <strong style={{ color: "#aaa" }}>Weight:</strong>{" "}
                {user.weight ? `${user.weight} kg` : "-"}
              </p>
            </div>
            {message && (
              <p
                style={{
                  color: "#9929EA",
                  marginTop: "20px",
                  fontWeight: "bold",
                }}
              >
                {message}
              </p>
            )}
          </div>
        </div>
      </div>

      {/* Edit Modal */}
      {showModal && (
        <div
          style={{
            position: "fixed",
            top: 0,
            left: 0,
            width: "100vw",
            height: "100vh",
            backgroundColor: "rgba(0,0,0,0.7)",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            zIndex: 999,
          }}
        >
          <div
            style={{
              background: "#111",
              padding: "30px",
              borderRadius: "15px",
              width: "400px",
              color: "white",
              boxShadow: "0 0 15px rgba(153,41,234,0.5)",
            }}
          >
            <h3 style={{ color: "#9929EA", textAlign: "center" }}>
              Edit Profile
            </h3>

            <div className="mb-3">
              <label>Name</label>
              <input
                type="text"
                name="name"
                value={formData.name || ""}
                onChange={handleChange}
                className="form-control"
              />
            </div>
            <div className="mb-3">
              <label>Age</label>
              <input
                type="number"
                name="age"
                value={formData.age || ""}
                onChange={handleChange}
                className="form-control"
              />
            </div>
            <div className="mb-3">
              <label>Weight (kg)</label>
              <input
                type="number"
                name="weight"
                value={formData.weight || ""}
                onChange={handleChange}
                className="form-control"
              />
            </div>
            <div className="mb-3">
              <label>Password</label>
              <input
                type="password"
                name="password"
                value={formData.password || ""}
                onChange={handleChange}
                className="form-control"
              />
            </div>

            <div className="d-flex justify-content-between mt-4">
              <button
                className="btn"
                style={{
                  backgroundColor: "#9929EA",
                  color: "white",
                  borderRadius: "8px",
                }}
                onClick={handleSave}
              >
                Save
              </button>
              <button
                className="btn"
                style={{
                  backgroundColor: "white",
                  color: "black",
                  borderRadius: "8px",
                }}
                onClick={() => setShowModal(false)}
              >
                Cancel
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
