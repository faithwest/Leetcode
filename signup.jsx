import React, { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { IoLeafOutline } from "react-icons/io5";
import Modal from "react-modal";

const SignupForm = () => {
  const [signupFormData, setSignupFormData] = useState({
    username: "",
    email: "",
    phone: "",
    password: "",
    location: "",
    imageUrl: "",
  });

  const [loading, setLoading] = useState(false);
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [selectedRole, setSelectedRole] = useState("");
  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setSignupFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleImageUpload = (e) => {
    const file = e.target.files[0];
    const reader = new FileReader();

    reader.onloadend = () => {
      setSignupFormData((prevData) => ({
        ...prevData,
        imageUrl: reader.result,
      }));
    };

    if (file) {
      reader.readAsDataURL(file);
    }
  };

  const handleSignup = async () => {
    if (selectedRole) {
      try {
        setLoading(true);

        // Simulate a loading delay
        setTimeout(async () => {
          // Additional logic to handle signup submission
          const imageLink =
            signupFormData.imageUrl || signupFormData.image; // Adjust based on your form data structure

          const response = await fetch("/user_signup", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              image_link: imageLink,
              username: signupFormData.username,
              email: signupFormData.email,
              phone: signupFormData.phone,
              address: signupFormData.location,
              password: signupFormData.password,
              role: selectedRole,
            }),
          });

          if (response.ok) {
            const data = await response.json();
            console.log(data);
            // Navigate to OTP page based on the selected role
            navigate(`/login`);
            toast.success("Signup successful! Please login.");
          } else {
            console.error("Server Error:", response.statusText);
            toast.error("An error occurred during signup");
          }

          setLoading(false);
        }, 2000); // Simulate a 2-second delay
      } catch (error) {
        console.error("Error during signup:", error);
        toast.error("An error occurred during signup");
        setLoading(false);
      }
    } else {
      // Open the role selection modal if a role is not chosen
      setModalIsOpen(true);
    }
  };
  const handleRoleSelection = (role) => {
    setSelectedRole(role);
    setModalIsOpen(false);
  };

  return (
    <div className="flex items-center justify-center h-screen bg-gradient-to-b from-white to-green-700 backdrop-filter backdrop-blur-sm">
      <div className="max-w-md w-full bg-white shadow-lg rounded-lg overflow-hidden">
        <div className="py-8 px-6">
          <div className="mt-8">
            <h2 className="text-3xl font-bold text-black-900 text-center">
              Signup
            </h2>
            <ToastContainer />
            <div className="mb-4 flex justify-center">
              {signupFormData.imageUrl && (
                <img
                  src={signupFormData.imageUrl}
                  alt="Uploaded"
                  className="rounded-full h-32 w-32 object-cover"
                />
              )}
            </div>
            <form className="mt-4">
              <div className="mb-4">
                <label htmlFor="username" className="block text-black-800">
                  Username:
                </label>
                <input
                  type="text"
                  id="username"
                  name="username"
                  value={signupFormData.username}
                  onChange={handleChange}
                  className="w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500"
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
                  value={signupFormData.email}
                  onChange={handleChange}
                  className="w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500"
                />
              </div>
              <div className="mb-4">
                <label htmlFor="phone" className="block text-black-800">
                  Phone Number:
                </label>
                <input
                  type="text"
                  id="phone"
                  name="phone"
                  value={signupFormData.phone}
                  onChange={handleChange}
                  className="w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500"
                />
              </div>
              <div className="mb-4">
                <label htmlFor="password" className="block text-black-800">
                  Password:
                </label>
                <input
                  type="password"
                  id="password"
                  name="password"
                  value={signupFormData.password}
                  onChange={handleChange}
                  className="w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500"
                />
              </div>
              <div className="mb-4">
                <label htmlFor="location" className="block text-black-800">
                  Location:
                </label>
                <input
                  type="text"
                  id="location"
                  name="location"
                  value={signupFormData.location}
                  onChange={handleChange}
                  className="w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500"
                />
              </div>
              <div className="mb-4">
                <label htmlFor="image" className="block text-black-800">
                  Upload Image:
                </label>
                <input
                  type="file"
                  id="image"
                  name="image"
                  accept="image/*"
                  onChange={handleImageUpload}
                  className="hidden"
                />
                <label
                  htmlFor="image"
                  className="w-full px-4 py-2 bg-green-500 text-white rounded-md hover:bg-blue-500 focus:outline-none focus:bg-blue-500 cursor-pointer"
                >
                  Choose File
                </label>
              </div>
              <button
                type="button"
                onClick={handleSignup}
                disabled={loading}
                className="w-full px-4 py-2 bg-green-500 text-white rounded-md hover:bg-blue-500 focus:outline-none focus:bg-blue-500"
              >
                {loading ? "Signing up..." : "Sign up"}
              </button>
            </form>
            <p className="mt-4 text-center">
              Already have an account?{" "}
              <Link to="/login" className="text-blue-500 hover:underline">
                Login
              </Link>
            </p>
          </div>
        </div>
      </div>
      <Modal
        isOpen={modalIsOpen}
        onRequestClose={() => setModalIsOpen(false)}
        className="modal absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2"
        overlayClassName="overlay fixed inset-0 bg-black opacity-50"
      >
        <div className="p-4 bg-white rounded-lg shadow-lg">
          <h2 className="text-lg font-bold mb-2">Choose Your Role</h2>
          <button
            className="bg-blue-500 text-white px-4 py-2 rounded-md mr-2"
            onClick={() => handleRoleSelection("buyer")}
          >
            Buyer
          </button>
          <button
            className="bg-green-500 text-white px-4 py-2 rounded-md"
            onClick={() => handleRoleSelection("farmer")}
          >
            Farmer
          </button>
        </div>
      </Modal>
    </div>
  );
};

export default SignupForm;
