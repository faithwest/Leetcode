import React, { useState, useEffect } from "react";
import { useNavigate, useLocation, Link } from "react-router-dom";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

const ResetPasswordForm = () => {
  const [token, setToken] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    const { email, token } = location.state || {};
    if (email && token) {
      setEmail(email);
      setToken(token);
    }
  }, [location.state]);

  const [email, setEmail] = useState("");

  const handleResetPassword = async () => {
    try {
      setLoading(true);

      if (!token || !newPassword || !confirmPassword) {
        throw new Error("Please fill in all fields");
      }

      if (newPassword !== confirmPassword) {
        throw new Error("Passwords do not match");
      }

      const response = await fetch("/reset_password", {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ token, new_password: newPassword, email }),
      });

      if (!response.ok) {
        const data = await response.json();
        throw new Error(data.message || "Failed to reset password");
      }

      toast.success("Password reset successful!");
      navigate("/login");
    } catch (error) {
      console.error("Error resetting password:", error);
      toast.error(
        error.message || "An error occurred while resetting your password"
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gradient-to-b from-white to-green-700">
      <div className="max-w-md w-full bg-white shadow-lg rounded-lg overflow-hidden">
        <div className="py-8 px-6">
          <h2 className="text-2xl font-bold text-black-900 text-center mb-4">
            Reset Your Password
          </h2>
          <ToastContainer />
          <form className="mt-4">
            <div className="mb-4">
              <label htmlFor="token" className="block text-black-800">
                Token:
              </label>
              <input
                type="text"
                id="token"
                name="token"
                value={token}
                readOnly
                className="w-full px-3 py-2 border rounded-md focus:outline-none focus:border-green-500"
              />
            </div>
            <div className="mb-4">
              <label htmlFor="email" className="block text-black-800">
                Email:
              </label>
              <input
                type="email"
                id="email"
                name="email"
                value={email}
                readOnly
                className="w-full px-3 py-2 border rounded-md focus:outline-none focus:border-green-500"
              />
            </div>
            <div className="mb-4">
              <label htmlFor="newPassword" className="block text-black-800">
                New Password:
              </label>
              <input
                type="password"
                id="newPassword"
                name="newPassword"
                value={newPassword}
                onChange={(e) => setNewPassword(e.target.value)}
                className="w-full px-3 py-2 border rounded-md focus:outline-none focus:border-green-500"
              />
            </div>
            <div className="mb-4">
              <label htmlFor="confirmPassword" className="block text-black-800">
                Confirm New Password:
              </label>
              <input
                type="password"
                id="confirmPassword"
                name="confirmPassword"
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                className="w-full px-3 py-2 border rounded-md focus:outline-none focus:border-green-500"
              />
            </div>
            <button
              type="button"
              onClick={handleResetPassword}
              disabled={loading}
              className="w-full px-4 py-2 bg-green-500 text-white rounded-md hover:bg-blue-500 focus:outline-none focus:bg-blue-500"
              style={{ transition: "background-color 0.3s ease" }}
            >
              {loading ? "Resetting..." : "Reset Password"}
            </button>
            <p className="mt-4 text-center">
              <Link to="/login" className="text-black-500 hover:underline">
                Back to Login
              </Link>
            </p>
          </form>
        </div>
      </div>
    </div>
  );
};

export default ResetPasswordForm;
