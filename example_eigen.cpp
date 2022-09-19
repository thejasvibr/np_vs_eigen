#include <iostream>
#include <chrono>
#include <Eigen/Dense>
#include <Eigen/QR>
#include <cmath>
#include <vector>

using Eigen::MatrixXd;
using Eigen::VectorXd;
using Eigen::Vector3f;
using namespace std;


vector<VectorXd> spiesberger_wahlberg_solution(MatrixXd array_geom,  VectorXd d,  double c=343.0){
  MatrixXd R, R_inv;
  VectorXd s1(3),s2(3);
  double a1,a2,a3; 
  double a_quad, b_quad, c_quad;
  double t_soln1, t_soln2;
  VectorXd b(array_geom.rows()-1);
  VectorXd f(array_geom.rows()-1);
  VectorXd g(array_geom.rows()-1);
  VectorXd tau(array_geom.rows()-1);

  tau = d/c;
  R = MatrixXd::Zero(array_geom.rows()-1, array_geom.cols());
  vector<VectorXd> both_solutions;
  
  //Assign R to all data from row 1 onwards.
  for (int i=0; i < array_geom.rows()-1; i++){
	  for (int j=0; j < array_geom.cols(); j++){
	  		R(i,j)  = array_geom(i+1,j);
	  }
   }
  // performing a pseudo-inverse. Not the recommended way in Eigen - it works right now...
  R_inv = R.completeOrthogonalDecomposition().pseudoInverse();
  for (int i=0; i < array_geom.rows()-1; i++){
	b(i) = pow(R.row(i).norm(),2) - pow(c*tau(i),2);
	f(i) = (c*c)*tau(i);
	g(i) = 0.5*(c*c-c*c);  
  	}
  a1 = (R_inv*b).transpose()*(R_inv*b);
  a2 = (R_inv*b).transpose()*(R_inv*f);
  a3 = (R_inv*f).transpose()*(R_inv*f);
	
  a_quad = a3 - pow(c,2);
  b_quad = -1*a2;
  c_quad = a1/4.0;		
  
  t_soln1 = (-b_quad + sqrt(pow(b_quad,2) - 4*a_quad*c_quad))/(2*a_quad);
  t_soln2 = (-b_quad - sqrt(pow(b_quad,2) - 4*a_quad*c_quad))/(2*a_quad);	

  s1 = R_inv*b*0.5 - (R_inv*f)*t_soln1;
  s2 = R_inv*b*0.5 - (R_inv*f)*t_soln2;
  both_solutions.push_back(s1);
  both_solutions.push_back(s2);
  return both_solutions;
	}


int main()
{
  

  /*MatrixXd array_geom(5,3);
  array_geom << 0,6,0, 0,13,0, 1,0,0, 0,0,1, 2,2,4;
  VectorXd d(array_geom.rows()-1);
  d << 0.01, 0.2, -0.3, 0.5;

  auto start = chrono::steady_clock::now();
  vector<VectorXd> both_solutions;
  both_solutions = spiesberger_wahlberg_solution(array_geom, d, 343.0);
  auto end = chrono::steady_clock::now();
  auto diff = end - start;
  std::cout << chrono::duration_cast<chrono::nanoseconds>(diff).count() << " ns" << std::endl;	
	
  // cout << "s1 " << both_solutions << "s2 " << s2 << std::endl;
  cout << "s1 " << both_solutions[0] << "s2 " << both_solutions[1] << std::endl;*/
  return 0;
}
