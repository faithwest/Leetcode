import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { IoLeafOutline } from "react-icons/io5";

const ForgotPasswordForm = () => {
  const [email, setEmail] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleChange = (e) => {
    setEmail(e.target.value);
  };

  const handleResetPassword = async () => {
    try {
      setLoading(true);

      if (!validateEmail(email)) {
        throw new Error("Invalid email format");
      }

      const response = await fetch("/forgot_password", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email }),
      });

      if (!response.ok) {
        const data = await response.json();
        throw new Error(data.message || "Failed to reset password");
      }

      const data = await response.json();

      // Assuming your backend returns a success message and the token
      // in the response data
      toast.success(
        data.message || "Password reset instructions sent to your email"
      );

      navigate("/resetpassword", { state: { email, token: data.token } });
    } catch (error) {
      console.error("Error resetting password:", error);
      toast.error(
        error.message || "An error occurred while resetting your password"
      );
    } finally {
      setLoading(false);
    }
  };

  const validateEmail = (email) => {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gradient-to-b from-white to-green-700">
      <div className="max-w-md w-full bg-white shadow-lg rounded-lg overflow-hidden">
        <div className="py-8 px-6">
          <div className="flex items-center justify-center">
            <IoLeafOutline className="text-green-500 text-4xl" />
            <h1 className="text-3xl font-bold text-black ml-2">
              Forgot Password
            </h1>
          </div>
          <div className="mt-8">
            {/* <h2 className="text-2xl font-bold text-gray-800 text-center">
              Reset Your Password
            </h2> */}
            <h5 className="text-center">
              The token will be sent to your email
            </h5>
            <ToastContainer />
            <form className="mt-4">
              <div className="mb-6">
                <label htmlFor="email" className="block text-black-900">
                  Email Address:
                </label>
                <input
                  type="email"
                  id="email"
                  name="email"
                  value={email}
                  onChange={handleChange}
                  className="w-full px-4 py-2 border rounded-md focus:outline-none focus:border-green-500"
                  placeholder="Enter your email"
                />
              </div>
              <button
                type="button"
                onClick={handleResetPassword}
                disabled={loading}
                className="w-full px-4 py-2 bg-green-700 text-white rounded-md hover:bg-blue-800 focus:outline-none focus:bg-green-800"
              >
                {loading ? "Sending..." : "Send Reset Token"}
              </button>
            </form>
            <p className="mt-4 text-center">
              Remember your password?{" "}
              <a href="/login" className="text-green-500 hover:underline">
                Log in
              </a>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ForgotPasswordForm;
