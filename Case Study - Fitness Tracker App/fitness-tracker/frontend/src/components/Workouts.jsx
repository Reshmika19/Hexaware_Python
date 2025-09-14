import React, { useState, useEffect } from "react";
import Footer from "./Footer";
import "bootstrap/dist/css/bootstrap.min.css";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { FaEdit, FaTrash } from "react-icons/fa";
import "./WorkoutPage.css";

const WorkoutPage = () => {
  const [workouts, setWorkouts] = useState([]);
  const [form, setForm] = useState({
    type: "",
    duration: "",
    calories: "",
    date: new Date().toISOString().split("T")[0],
  });
  const [filterRange, setFilterRange] = useState("5days");

  // Edit Modal
  const [showEditModal, setShowEditModal] = useState(false);
  const [editForm, setEditForm] = useState(null);
  const [editMessage, setEditMessage] = useState("");

  // Delete Modal
  const [showDeleteModal, setShowDeleteModal] = useState(false);
  const [deleteWorkoutId, setDeleteWorkoutId] = useState(null);
  const [deleteMessage, setDeleteMessage] = useState("");

  const navigate = useNavigate();

  // Date restrictions
  const today = new Date();
  const minDate = new Date(today);
  minDate.setDate(today.getDate() - 2);
  const maxDate = today.toISOString().split("T")[0];
  const minDateStr = minDate.toISOString().split("T")[0];

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  // Fetch workouts
  const fetchWorkouts = async (range = filterRange) => {
    const token = localStorage.getItem("token");
    if (!token) return;
    try {
      const res = await axios.get(
        `http://127.0.0.1:5000/workouts/filter?range=${range}`,
        { headers: { Authorization: `Bearer ${token}` } }
      );
      setWorkouts(res.data);
    } catch (err) {
      console.error("Error fetching workouts:", err);
    }
  };

  useEffect(() => {
    fetchWorkouts();
  }, []);

  const handleFilterChange = (e) => {
    const selectedRange = e.target.value;
    setFilterRange(selectedRange);
    fetchWorkouts(selectedRange);
  };

  // Add Workout
  const handleSubmit = async (e) => {
    e.preventDefault();
    const token = localStorage.getItem("token");
    try {
      await axios.post(
        "http://127.0.0.1:5000/workouts",
        {
          exercise_type: form.type,
          duration: form.duration,
          calories: form.calories,
          date: form.date,
        },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      fetchWorkouts(filterRange);
      setForm({
        type: "",
        duration: "",
        calories: "",
        date: new Date().toISOString().split("T")[0],
      });
    } catch (err) {
      console.error(err);
    }
  };

  // Open Edit Modal
  const openEditModal = (workout) => {
    setEditForm({ ...workout });
    setEditMessage("");
    setShowEditModal(true);
  };

  // Save Edit
  const handleEditSave = async () => {
    const token = localStorage.getItem("token");
    try {
      await axios.put(
        `http://127.0.0.1:5000/workouts/${editForm.workout_id}`,
        editForm,
        { headers: { Authorization: `Bearer ${token}` } }
      );
      setEditMessage("Workout updated successfully");
      fetchWorkouts(filterRange);
    } catch (err) {
      console.error("Error editing workout:", err);
    }
  };

  // Open Delete Modal
  const openDeleteModal = (id) => {
    setDeleteWorkoutId(id);
    setDeleteMessage("");
    setShowDeleteModal(true);
  };

  // Confirm Delete
  const handleDeleteConfirm = async () => {
    const token = localStorage.getItem("token");
    try {
      await axios.delete(`http://127.0.0.1:5000/workouts/${deleteWorkoutId}`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      setDeleteMessage("Workout deleted successfully");
      fetchWorkouts(filterRange);
    } catch (err) {
      console.error("Error deleting workout:", err);
    }
  };

  return (
    <div style={{ backgroundColor: "#000", color: "#fff", minHeight: "100vh" }}>
      <div className="container py-5">
       
        <button
          className="btn btn-theme mb-4"
          onClick={() => navigate("/dashboard")}
        >
           Back to Dashboard
        </button>

        <div className="row">
          {/* Left - Add Form */}
          <div className="col-md-6 mb-4">
            <h2 className="mb-4 text-theme">Add Workout</h2>
            <form onSubmit={handleSubmit} className="p-4 rounded bg-dark-theme">
              <div className="mb-3">
                <label className="form-label">Exercise Type</label>
                <input
                  type="text"
                  className="form-control theme-input"
                  name="type"
                  value={form.type}
                  onChange={handleChange}
                  required
                />
              </div>

              <div className="mb-3">
                <label className="form-label">Duration (mins)</label>
                <input
                  type="number"
                  className="form-control theme-input"
                  name="duration"
                  value={form.duration}
                  onChange={handleChange}
                  required
                />
              </div>

              <div className="mb-3">
                <label className="form-label">Calories Burned</label>
                <input
                  type="number"
                  className="form-control theme-input"
                  name="calories"
                  value={form.calories}
                  onChange={handleChange}
                  required
                />
              </div>

              <div className="mb-3">
                <label className="form-label">Date</label>
                <input
                  type="date"
                  className="form-control theme-input"
                  name="date"
                  value={form.date}
                  onChange={handleChange}
                  min={minDateStr}
                  max={maxDate}
                  required
                />
              </div>

              <button type="submit" className="btn btn-theme w-100">
                Add Workout
              </button>
            </form>
          </div>

          {/* Right - Table */}
          <div className="col-md-6">
            <div className="d-flex justify-content-between align-items-center mb-3">
              <h2 className="text-theme">Workout History</h2>
              <select
                className="form-select w-auto theme-input"
                value={filterRange}
                onChange={handleFilterChange}
              >
                <option value="3days">Last 3 Days</option>
                <option value="5days">Last 5 Days</option>
                <option value="month">This Month</option>
              </select>
            </div>

            {workouts.length === 0 ? (
              <p>No workouts yet. Start adding!</p>
            ) : (
              <table className="table table-dark table-striped">
                <thead>
                  <tr>
                    <th>Date</th>
                    <th>Type</th>
                    <th>Duration</th>
                    <th>Calories</th>
                    <th>Action</th>
                  </tr>
                </thead>
                <tbody>
                  {workouts.map((w, index) => (
                    <tr key={index}>
                      <td>{w.date}</td>
                      <td>{w.exercise_type}</td>
                      <td>{w.duration} mins</td>
                      <td>{w.calories} kcal</td>
                      <td>
                        <FaEdit
                          className="icon-edit"
                          onClick={() => openEditModal(w)}
                        />
                        <FaTrash
                          className="icon-delete"
                          onClick={() => openDeleteModal(w.workout_id)}
                        />
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            )}
          </div>
        </div>
      </div>

      {/* Edit Modal */}
      {showEditModal && (
        <div className="modal fade show d-block " style={{ background: "rgba(0,0,0,0.7)" }}>
          <div className="modal-dialog">
            <div className="modal-content" style={{ background: "#111", color: "#fff" }}>
              <div className="modal-header">
                <h5 className="modal-title" style={{ color: "#9929EA" }}>Edit Workout</h5>
                <button
                  className="btn-close btn-close-white"
                  onClick={() => setShowEditModal(false)}
                ></button>
              </div>
              <div className="modal-body">
                {editMessage ? (
                  <div style={{ color: "#9929EA", fontWeight: "bold" }}>{editMessage}</div>
                ) : (
                  <>
                    <div className="mb-3">
                      <label>Exercise Type</label>
                      <input
                        type="text"
                        className="form-control theme-input"
                        value={editForm.exercise_type}
                        onChange={(e) =>
                          setEditForm({
                            ...editForm,
                            exercise_type: e.target.value,
                          })
                        }
                      />
                    </div>
                    <div className="mb-3">
                      <label>Duration (mins)</label>
                      <input
                        type="number"
                        className="form-control theme-input"
                        value={editForm.duration}
                        onChange={(e) =>
                          setEditForm({
                            ...editForm,
                            duration: e.target.value,
                          })
                        }
                      />
                    </div>
                    <div className="mb-3">
                      <label>Calories</label>
                      <input
                        type="number"
                        className="form-control theme-input"
                        value={editForm.calories}
                        onChange={(e) =>
                          setEditForm({
                            ...editForm,
                            calories: e.target.value,
                          })
                        }
                      />
                    </div>
                    <div className="mb-3">
                      <label>Date</label>
                      <input
                        type="date"
                        className="form-control theme-input"
                        value={editForm.date}
                        onChange={(e) =>
                          setEditForm({ ...editForm, date: e.target.value })
                        }
                      />
                    </div>
                  </>
                )}
              </div>
              <div className="modal-footer">
                {!editMessage && (
                  <button className="btn"
                    style={{ backgroundColor: "#9929EA", color: "#fff" }} onClick={handleEditSave}>
                    Save Changes
                  </button>
                )}
                <button
                  className="btn btn-secondary"
                  onClick={() => setShowEditModal(false)}
                >
                  Close
                </button>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Delete Modal */}
      {showDeleteModal && (
        <div className="modal show d-block" style={{ background: "rgba(0,0,0,0.7)" }}>
          <div className="modal-dialog">
            <div className="modal-content" style={{ background: "#111", color: "#fff" }}>
              <div className="modal-header">
                <h5 className="modal-title" style={{ color: "#9929EA" }}>Delete Workout</h5>
                <button className="btn-close btn-close-white" onClick={() => setShowDeleteModal(false)}></button>
              </div>
              <div className="modal-body">
                {deleteMessage ? (
                  <p style={{ color: "#9929EA", fontWeight: "bold" }}>{deleteMessage}</p>
                ) : (
                  <p>Are you sure you want to delete this workout?</p>
                )}
              </div>
              <div className="modal-footer">
                {!deleteMessage && (
                  <button
                    className="btn"
                    style={{ backgroundColor: "#9929EA", color: "#fff" }}
                    onClick={handleDeleteConfirm}
                  >
                    Yes, Delete
                  </button>
                )}
                <button className="btn btn-secondary" onClick={() => setShowDeleteModal(false)}>
                  Close
                </button>
              </div>
            </div>
          </div>
        </div>
      )}


      <Footer />
    </div>
  );
};

export default WorkoutPage;

